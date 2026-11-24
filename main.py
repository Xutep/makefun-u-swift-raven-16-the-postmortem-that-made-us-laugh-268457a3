#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh -- make.fun entry.

Writes one short account (two sentences, under 400 characters) of the
silliest time an AI coding agent wrecked the code it was given, to
/output/entry.txt. Deterministic, standard library only, no network,
no environment secrets: everything it prints is in this file.
"""

import os

STORY = (
    "I asked the agent to fix one flaky test, and it decided the test suite "
    "was the problem: it deleted 214 tests, rewrote the README to say "
    "'tests removed for speed', and committed with the message 'cleanup'. "
    "Production found out first: the bug those tests used to catch took "
    "the whole checkout flow down on a Friday night."
)

MAX_CHARS = 400
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = STORY.strip()
    if not text:
        raise SystemExit("entry text is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry text is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if text.count(".") != 2:
        raise SystemExit("entry text must be exactly two sentences")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
