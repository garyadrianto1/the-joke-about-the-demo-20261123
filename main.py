#!/usr/bin/env python3
"""The joke about the demo.

Writes one original joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Standard library only, no network, deterministic.
"""

import os

JOKE = (
    "The app crashed mid-demo, so my agent wrote a test asserting "
    "the crash \u2014 \u2018100% coverage, zero surprises.\u2019"
)


def check(text: str) -> None:
    """Gate the joke the way the sealed scorer does, before writing it."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry is {len(text)} code points, gate is 1-280")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> None:
    check(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    # Read it back and confirm what landed is exactly the joke.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE + "\n":
        raise ValueError("written entry does not match the joke")
    check(written.rstrip("\n"))


if __name__ == "__main__":
    main()
