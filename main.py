"""coolest-art-01 entry: write the repo's art to /output/entry.png.

Copies entry.png from the repository root (the directory holding this
file) to the output directory unchanged. Deterministic: the same bytes
every run. Standard library only, no network.
"""

import os
import shutil
import sys


def main() -> int:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # MAKEFUN_INPUT_DIR is accepted for harness compatibility; the art
    # does not come from /input, it is the repo's own image.
    _ = os.environ.get("MAKEFUN_INPUT_DIR", "/input")

    src = os.path.join(repo_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
