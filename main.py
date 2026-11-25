#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

One line of patch notes announcing that human sleep has been fixed.
The program writes exactly one line to entry.txt: a changelog-style
fix for the most common sleep bug in the field, the brain replaying
an old embarrassment at bedtime instead of shutting down.

Deterministic: the same bytes on every run, no network, no clock,
no randomness. The output is verified against its pinned hash and
byte count before it is written.
"""

import hashlib
import os
import sys

LINE = (
    "Fixed: sleep no longer requires 45 minutes of staring at the "
    "ceiling while replaying an embarrassing moment from 2014."
)

EXPECTED_CHARS = 118
EXPECTED_BYTES = 118
EXPECTED_SHA256 = "17dabdf865c610e04acbdee5498a83747ff08017b9977810e4aeabd1d300ecbb"


def output_dir() -> str:
    """Where entry.txt goes: the harness directory when set, else /output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return "out"


def main() -> int:
    data = LINE.encode("utf-8")
    if len(LINE) != EXPECTED_CHARS:
        print(f"refusing: line is {len(LINE)} chars, expected {EXPECTED_CHARS}",
              file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"refusing: line is {len(data)} bytes, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"refusing: sha256 {digest} != {EXPECTED_SHA256}",
              file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 160) or not LINE.strip():
        print("refusing: line fails the 1-160 char gate", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("refusing: line must stay a single line", file=sys.stderr)
        return 1

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
