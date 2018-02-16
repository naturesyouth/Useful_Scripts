#!/usr/bin/python3

import os
import fnmatch


def get_source_list(directory="."):
    for root, dir, files in os.walk(directory):
        for items in fnmatch.filter(files, "*.py"):
            print(root + items)


if __name__ == "__main__":
    get_source_list()
