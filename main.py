"""One Word From Grandma — entry program.

Writes exactly one word, the single word grandma would text about AI,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
bounty's RULES.txt requires. Deterministic: no randomness, no network,
no input files.
"""

import os

WORD = "Al"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {path} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
