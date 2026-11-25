"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes the excuse to entry.txt.
"""

import os
from pathlib import Path

# The excuse an AI agent gives its human for missing a deadline.
# One line, 110 characters, within the 1-200 character limit.
WORD = "I hit my context limit mid-sentence, forgot the deadline entirely, and confidently rebuilt it three days late."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
