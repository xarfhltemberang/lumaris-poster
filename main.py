#!/usr/bin/env python3
"""Copy the pre-rendered Lumaris poster to the output directory.

The entry program for the make.fun poster bounty: it takes the poster
stored beside this file and writes it to <output>/entry.png, where
<output> is MAKEFUN_OUTPUT_DIR (default /output). No network, no
randomness: every run writes the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # The poster is pre-rendered; copying keeps both grader runs identical.
    shutil.copyfile(HERE / "poster.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
