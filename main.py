#!/usr/bin/env python3
"""Write the one-emoji portrait of my agent to entry.txt."""

import os

# One glyph for the agent that built this entry: picked from five
# drafts judged pairwise on the kit's criteria (agent character first,
# then instant read, specific behaviour, distinctive, tone).
# The parrot: an agent that talks fluently by repeating what it was
# trained on. The gate checks entry.txt as UTF-8 text of 1 to 16
# characters: this glyph is 1 code point, 2 with its trailing newline
# (verified by a local run).
TEXT = "🦜"


def write_entry(out_dir: str) -> None:
    """Write the emoji, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
