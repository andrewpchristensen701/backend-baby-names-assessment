#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

__author__ = "andrewpchristensen701"

def extract_names(filename):

    with open(filename, "r") as file:
        text = file.read()

    year_match_obj = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    year = year_match_obj.group(1)
    result = [year]

    names_dict = {}
    # Creates tuple list of rank, boy names, girl names
    tuple_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    # Unpack tuple directly into variables this way
    for rank, boy, girl in tuple_list:
        names_dict[boy] = rank
        names_dict[girl] = rank
    # Creates sorted list of all names
    names_list = sorted(names_dict.keys())
    for name in names_list:
        result.append(name + " " + names_dict[name])

    return result




def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')

    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    for file in args.files:
        result_string = "\n".join(extract_names(file))
        if args.summaryfile:
            with open(file + ".summary", "w") as f:
                f.write(result_string)
        else:
            print(result_string)


if __name__ == '__main__':
    main()