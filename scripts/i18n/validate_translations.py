#!/usr/bin/env python3
"""Validate OptiScaler translations without third-party dependencies."""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FILE = ROOT / "lang" / "zh-CN.txt"
CONVERSIONS = set("diuoxXfFeEgGaAcspnCSZ")
FLAGS = set("-+ #0'")
LENGTHS = ("I64", "I32", "hh", "ll", "h", "l", "j", "z", "t", "L", "I")


def unescape(text: str) -> str:
    return re.sub(r"\\([=nt\\])", lambda match: {
        "=": "=", "n": "\n", "t": "\t", "\\": "\\"
    }[match.group(1)], text)


def split_record(line: str) -> tuple[str, str]:
    i = 0
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):
            i += 2
            continue
        if line[i] == "=":
            return unescape(line[:i].strip()), unescape(line[i + 1:].strip())
        i += 1
    raise ValueError("missing unescaped '=' delimiter")


def specs(text: str) -> list[str]:
    result = []
    i = 0
    while i < len(text):
        if text[i] != "%":
            i += 1
            continue
        start = i
        i += 1
        if i >= len(text):
            raise ValueError("stray '%'")
        if text[i] == "%":
            i += 1
            continue
        position = i
        while i < len(text) and text[i].isdigit():
            i += 1
        if i < len(text) and text[i] == "$":
            i += 1
        else:
            i = position
        while i < len(text) and text[i] in FLAGS:
            i += 1

        def width(at: int) -> int:
            if at < len(text) and text[at] == "*":
                at += 1
                start_pos = at
                while at < len(text) and text[at].isdigit():
                    at += 1
                return at + 1 if at < len(text) and text[at] == "$" else start_pos
            while at < len(text) and text[at].isdigit():
                at += 1
            return at

        i = width(i)
        if i < len(text) and text[i] == ".":
            i = width(i + 1)
        for suffix in LENGTHS:
            if text.startswith(suffix, i):
                i += len(suffix)
                break
        if i >= len(text) or text[i] not in CONVERSIONS:
            raise ValueError(f"invalid printf conversion at offset {start}")
        i += 1
        result.append(text[start:i])
    return result


def validate(path: pathlib.Path) -> None:
    seen = set()
    errors = []
    count = 0
    for number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw.strip()
        if not line or line[0] in "#;":
            continue
        try:
            source, target = split_record(line)
            if not source or not target:
                raise ValueError("empty key or translation")
            if source in seen:
                raise ValueError("duplicate source")
            seen.add(source)
            if specs(source) != specs(target):
                raise ValueError("different printf conversion signatures")
            count += 1
        except ValueError as exc:
            errors.append(f"{path}:{number}: {exc}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"i18n OK: validated {count} unique translations")


if __name__ == "__main__":
    validate(FILE)
