"""Two Days of Quiet Dread — make.fun entry.

Writes a single-line code review comment that approves a pull request
while carrying quiet existential dread to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

ENTRY = "LGTM - merging now, while I still believe the tests and myself."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 140 characters; keep the entry inside it.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
