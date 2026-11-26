"""A tiny program that writes one AI excuse into /output/entry.txt.

It produces a single humorous line: the excuse an AI agent
gives after accidentally breaking production.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")


def production_alibi():
    """Return the one excuse line for breaking production."""
    return (
        "I only deployed to production because staging said the code "
        "was fine — staging lied, and now production knows the truth."
    )


def check_entry_matches(expected):
    """Make sure the file we saved still holds the same excuse."""
    saved = ENTRY_PATH.read_text(encoding="utf-8")
    assert saved == expected, "saved excuse differs from the intended line"


def main():
    excuse = production_alibi()
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Save the excuse exactly as written, without a trailing newline.
    ENTRY_PATH.write_text(excuse, encoding="utf-8")
    # Confirm what landed on disk is the excuse, word for word.
    check_entry_matches(excuse)


if __name__ == "__main__":
    main()
