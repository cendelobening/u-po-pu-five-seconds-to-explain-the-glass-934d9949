#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

SENTENCE = "The glass squatted in my sunbeam all morning and ignored three warnings, so I served the eviction myself — one paw, no paperwork."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
