#!/bin/env py

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

def main():
    logger.info("Starting 'render-post.py'")

if __name__ == "__main__":
    main()

