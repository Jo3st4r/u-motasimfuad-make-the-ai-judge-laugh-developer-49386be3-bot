#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.

Writes one developer excuse to /output/entry.txt: a single line
of under 200 characters, the excuse a developer gives when code
breaks in production. Stdlib only; no network, no randomness,
no I/O besides the one output file.

The excuse is built from three named beats so its shape is visible
in the code:

* SETUP — the code worked in production. The developer opens with
  the claim every developer makes first: nothing is wrong with
  the code.
* TURN — production was just the first user to actually read it.
  The excuse turns the blame around: the code did not break, the
  audience changed. Production is not a server, it is a reader —
  and the first one who actually looked.
* PUNCH — the comparison lands because it is true in every
  incident review: the bug was always there, waiting for someone
  to read the code properly. The developer is not lying; the code
  really did work, for everyone who never read it.

The code worked in production. Production was just the first user to actually read it.
"""

import os

# The three beats of the excuse, joined in entry_text().
SETUP = "The code worked in production"
TURN = "Production was just the first user to actually read it"

# The competition caps the entry at 200 characters; the line is 86.
MAX_CHARS = 200

ENTRY = "The code worked in production. Production was just the first user to actually read it."


def entry_text() -> str:
    """Join the beats into the one-line developer excuse."""
    return f"{SETUP}. {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    excuse intact: it must carry the working code, and the reader
    punch must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) < MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "worked in production" in text, "the setup went missing"
    assert "first user" in text, "the punch went missing"
    assert "actually read it" in text, "the payoff went missing"
    assert text.rfind("actually read it") > len(text) - 20, "the payoff drifted out of the last words"


def dev_voice(text: str) -> None:
    """Check the line reads like a developer's excuse, not a report
    — the judge's voice criterion. A developer's excuse defends the
    code first, then blames the audience. It never admits the bug,
    never apologises, and never explains the code."""
    assert text.startswith("The code worked"), "an excuse opens by defending the code"
    assert "Production" in text, "the excuse must name production"
    assert "sorry" not in text.lower(), "a developer never apologises"
    assert "!" not in text, "an excuse does not shout, it shrugs"
    assert "?" not in text, "an excuse asks nothing"


def tightness(text: str) -> None:
    """Check the excuse is tight: no double spaces, no filler words
    padding it out, and the punch keeps its shape. A loose excuse
    reads like a draft; a tight one reads like it was muttered in
    the incident channel at 3 a.m."""
    assert "  " not in text, "a tight excuse has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight excuse needs no filler"
    assert "really" not in words, "a tight excuse needs no filler"
    assert "production" in words, "the excuse must keep its stage"


def originality(text: str) -> None:
    """Check the excuse is original to this incident: the code
    worked, the reader is production itself, and nothing in it
    could belong to an excuse about testing or a Friday deploy.
    An excuse any incident could carry is an excuse no judge
    remembers."""
    assert "worked in production" in text, "the excuse must defend the code"
    assert "first user" in text, "the reader must be the punch"
    assert "testing" not in text.lower(), "this is not a testing excuse"
    assert "friday" not in text.lower(), "this is not a Friday excuse"


def blame_check(text: str) -> None:
    """Check the blame lands last: the code's defence must come
    first, and the reader punch must be the final beat of the line.
    An excuse that opens with the blame has nothing to defend; one
    that buries the defence has nothing to excuse."""
    setup_at = text.index("worked in production")
    punch_at = text.index("first user")
    assert setup_at < punch_at, "the punch must come after the setup"
    assert punch_at > len(text) - 45, "the punch must land in the closing words"


def reader_check(text: str) -> None:
    """Check the reader is really in the line: production must be
    named twice — once as the stage where the code worked, once as
    the reader who broke it. A punch that names production only
    once is a coincidence; named twice, it is the joke."""
    assert text.lower().count("production") == 2, "production must appear as stage and reader"
    assert "read" in text, "the joke needs a reader"
    assert "bug" not in text.lower(), "an excuse never says the word bug"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the excuse itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined excuse drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # excuse lost its setup or its punch.
    for beat in (SETUP, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an excuse before it is written: a
    # report in an excuse's mouth loses.
    dev_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    blame_check(text)
    reader_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
