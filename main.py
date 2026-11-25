"""Entry for "The Meeting That Should Have Been One Line" (make.fun).

Writes a single sentence to /output/entry.txt: the one line that could
have replaced an entire pointless meeting.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace. The file is written with no trailing
newline so the byte count stays exactly the entry's character count.
"""

import os

ENTRY = (
    "We already agreed on this in the email thread \u2014 this meeting is "
    "just an hour of watching people nod at a slide nobody read."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry if it passes the gate, else raise."""
    text = text.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 200 limit")
    # Exactly one sentence: a single terminal period, nothing else.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    return text


def main() -> None:
    text = validate(ENTRY)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Never remove the output directory: the grader mounts it, and
    # deleting it fails run_completes (EBUSY/EACCES as unprivileged user).
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
