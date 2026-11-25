"""Helpdesk one-liner: a cheerful agent talks a caller through a restart."""
import os

_LINE_PARTS = (
    "Sir, I understand you're upset. ",
    "Please turn the life support off, ",
    "count to ten, and turn it back on. ",
    "The beeping should stop either way.",
)


def _assemble_line(parts):
    return "".join(parts)


def _save_line(text):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    _save_line(_assemble_line(_LINE_PARTS))
