#!/bin/env py

import argparse
import markdown
import logging
import os
import re

logger = logging.getLogger("generate-post")
logger.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)

stream_formatter = logging.Formatter("%(asctime)s <%(name)s> [%(levelname)s]: %(message)s", datefmt="%H:%M:%S")
stream.setFormatter(stream_formatter)

logfile = logging.FileHandler("render-post.log", encoding="utf-8")
logfile.setLevel(logging.DEBUG)

logfile_formatter = logging.Formatter("%(asctime)s <%(name)s> [%(levelname)s]: %(message)s", datefmt="%y-%M-%d %H:%M:%S")
logfile.setFormatter(logfile_formatter)

logger.addHandler(stream)
logger.addHandler(logfile)

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="render-post.py",
        description="Renders a markdown post to html"
    )

    parser.add_argument("input")
    parser.add_argument("-o", "--output")

    return parser.parse_args()

def get_template():
    print("Template!")

def main():
    config = parse_arguments()
    logger.info(f"Rendering post '{config.input}'")

    template = get_template()


if __name__ == "__main__":
    main()

