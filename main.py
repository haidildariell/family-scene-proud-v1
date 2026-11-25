#!/usr/bin/env python3
"""Family scene entry.

Writes a two-line family scene to the output file.
Self-contained: no network, no external files, no dependencies.
"""

import os
import sys

SCENE = (
    'Grandpa held the phone like it might bite. "Tap the green one, Grandpa," I said.\n'
    'He tapped — and my face filled the screen. "There you are," he smiled. "Now I can carry you in my pocket."'
)

MIN_CHARS = 1
MAX_CHARS = 280
EXPECTED_LINES = 2


def check_length(text):
    """Length + blank check: 1-280 chars, not whitespace-only."""
    if not text.strip():
        raise ValueError("scene must not be blank")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"scene must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}")


def check_lines(text):
    """Line check: exactly 2 lines, each with real text."""
    lines = text.split("\n")
    if len(lines) != EXPECTED_LINES:
        raise ValueError(f"scene must have exactly {EXPECTED_LINES} lines, got {len(lines)}")
    for line in lines:
        if not line.strip():
            raise ValueError("each line must contain text")
    return lines


def validate_scene(text):
    """Full scene check: type, length, lines, UTF-8 encodable."""
    if not isinstance(text, str):
        raise TypeError("scene must be a string")
    check_length(text)
    check_lines(text)
    text.encode("utf-8")
    return text


def output_path():
    """Output path from ENTRY_OUTPUT, default /output/entry.txt."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def ensure_parent_dir(path):
    """Create the parent directory of path if it does not exist."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def write_entry(path, text):
    """Write the scene as UTF-8, creating the parent dir if needed."""
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main():
    scene = validate_scene(SCENE)
    path = write_entry(output_path(), scene)
    print(f"Wrote {len(scene)} chars, {len(scene.splitlines())} lines to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
