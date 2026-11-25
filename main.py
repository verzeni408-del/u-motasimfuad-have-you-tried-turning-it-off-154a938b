"""Cheerful support agent note: assembles the line and writes it out."""
import os

_NOTE_BITS = (
    "Great news, I found the issue, ",
    "just switch off the life support machine ",
    "for ten seconds and switch it back on, ",
    "good as new!",
)


def _stitch_note(bits):
    return "".join(bits)


def _drop_note(text):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    _drop_note(_stitch_note(_NOTE_BITS))
