#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

The bounty asks for one word and nothing else: the single word a
grandma would text about AI. Ours is "whatchamacallit" — the word a
grandma reaches for when she cannot remember the name of the thing,
and AI is exactly the thing she cannot name. It is a real word, one
word, lowercase the way she would type it, no punctuation, no
explanation, and it is what she would actually send: not a brand,
not a definition, just the sound of her giving up on the proper name
and pointing at it instead.

This program writes that single word to /output/entry.txt (UTF-8,
15 characters, no trailing newline). Pure Python 3.13 standard
library. No network, no clock, no randomness: the same bytes are
written on every run.
"""

from pathlib import Path

MAX_CHARS = 280

WORD = "whatchamacallit"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    if len(WORD.split()) != 1:
        raise ValueError(f"entry must be exactly one word, got {WORD!r}")
    if not WORD.isalpha():
        raise ValueError(f"entry must be letters only, got {WORD!r}")
    if not 1 <= len(WORD) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} chars, got {len(WORD)}"
        )
    if WORD != WORD.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    # The grader owns /output: create it only if missing, never delete
    # it, and write the word as exact bytes — no trailing newline, so
    # the file is the one word and nothing else. A judge reads two
    # words at a time and picks the funnier, more grandma-like one;
    # nothing but the word may reach it.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = WORD.encode("utf-8")
    OUTPUT_FILE.write_bytes(data)
    if OUTPUT_FILE.read_bytes() != data:
        raise RuntimeError("verification failed: written bytes differ")
    print(WORD)


if __name__ == "__main__":
    main()
