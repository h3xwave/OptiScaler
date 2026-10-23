"""Regression tests for translation validation, generation and menu coverage."""
import contextlib
import io
import pathlib
import tempfile
import unittest
from unittest import mock

import check_menu_coverage as coverage
import merge_all_translations as generator
from validate_translations import specs, split_record, validate


class TranslationTests(unittest.TestCase):
    def test_escaped_delimiter(self):
        self.assertEqual(split_record(r"left\=right = 左\=右"), ("left=right", "左=右"))
        self.assertEqual(split_record(r"path\\ = 路径"), ("path\\", "路径"))

    def test_full_printf_signature(self):
        self.assertEqual(specs("%*.*f %% %I64u %2$s"), ["%*.*f", "%I64u", "%2$s"])
        self.assertNotEqual(specs("%d"), specs("%s"))
        self.assertNotEqual(specs("%f"), specs("%*f"))
        with self.assertRaises(ValueError):
            specs("bad %")

    def test_value_drift_and_empty_values_are_rejected(self):
        for target in ("wrong", ""):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                pack = pathlib.Path(directory) / "test.txt"
                pack.write_text("Label = " + target, encoding="utf-8")
                with mock.patch.object(generator, "OUTPUT", pack), mock.patch.object(
                    generator, "merged_table", return_value={"Label": "正确"}
                ):
                    with self.assertRaises(ValueError):
                        generator.check()

    def test_duplicate_and_bad_format_rejected(self):
        for text in ("Label = 正确\nLabel = 重复\n", "%d = %s\n"):
            with self.subTest(text=text), tempfile.TemporaryDirectory() as directory:
                pack = pathlib.Path(directory) / "test.txt"
                pack.write_text(text, encoding="utf-8")
                with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
                    validate(pack)

    def test_generated_pack_roundtrip(self):
        with tempfile.TemporaryDirectory() as directory:
            pack = pathlib.Path(directory) / "zh-CN.txt"
            pack.write_text(generator.generate(), encoding="utf-8")
            with mock.patch.object(generator, "OUTPUT", pack), contextlib.redirect_stdout(io.StringIO()):
                generator.check()
                validate(pack)


class CoverageTests(unittest.TestCase):
    def test_comments_literals_ids_and_nested_arguments(self):
        source = r'''
            // ImGui::Button("Not visible");
            /* ShowTooltip("Not visible either"); */
            ImGui::Button("Reset##instance");
            ImGui::Text("Value: %d", value);
            ImGui::TextColored(Color(1, 2, 3), "Warning");
            ShowTooltip("First\n" "second");
            ImGui::Text("%s", runtimeString);
            ImGui::Text("%*.*f", width, precision, value);
            ImGui::Text("%2$s", first, second);
            ImGui::Button("##hidden");
            ImGui::BeginChild("InternalId");
            ShowTooltip("Text##literal");
        '''
        self.assertEqual(set(coverage.extract(source)), {
            "Reset", "Value: %d", "Warning", "First\nsecond", "Text##literal"
        })

    def test_sidebar_cards_and_dynamic_labels(self):
        source = '''
            static const Tab tabs[] = {
                { "group", "Latency", Draw },
            };
            static const MenuBox boxes[] = {
                { "internal", "Category", "Card", [](C& c) { Draw(c); } },
            };
            static const char* QuirksTabLabel(State& state) {
                if (state.quirks) return "Quirks and ASI";
                return state.asi ? "ASI" : "Quirks";
            }
        '''
        self.assertEqual(set(coverage.extract(source)), {
            "Latency", "Category", "Card", "Quirks and ASI", "ASI", "Quirks"
        })

    def test_option_descriptions_and_keybinds(self):
        source = r'''
            std::vector<MenuOption<FGInput>> inputs;
            inputs = { { FGInput::Upscaler, "Source##id", "First\n" "second" } };
            inputs[0].set_disabled(Check(1, 2), "Missing backend");
            inputs[0].tooltip = "Other " "description";
            auto menu = Keybind("Menu", 10);
            PopulateCombo("FG Input", selected, inputs);
        '''
        self.assertEqual(set(coverage.extract(source)), {
            "Source", "First\nsecond", "Missing backend", "Other description", "Menu", "FG Input"
        })

    def test_unknown_menu_label_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            menu, pack, allowlist = (root / name for name in ("menu.cpp", "pack.txt", "allow.json"))
            menu.write_text('ImGui::Button("New upstream label");', encoding="utf-8")
            pack.write_text("Known = 已知\n", encoding="utf-8")
            allowlist.write_text("{}", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
                coverage.check(menu, pack, allowlist)

    def test_current_menu_coverage(self):
        with contextlib.redirect_stdout(io.StringIO()):
            coverage.check()


if __name__ == "__main__":
    unittest.main()
