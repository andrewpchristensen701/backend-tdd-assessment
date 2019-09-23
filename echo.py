#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "andrewpchristensen701"


import sys
import argparse


def upper(str):
    return str.upper()


def lower(str):
    return str.lower()


def title(str):
    return str.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    """Implementation of echo"""

    if not args:
        parser.print_usage()
        sys.exit(1)
    text = args.text
    if args.upper and args.lower and args.title:
        text = upper(text)
        text = lower(text)
        text = title(text)
    elif args.lower and args.title:
        text = lower(text)
        text = title(text)
    elif args.upper and args.title:
        text = upper(text)
        text = title(text)
    elif args.upper and args.lower:
        text = upper(text)
        text = lower(text)
    elif args.upper:
        text = upper(text)
    elif args.lower:
        text = lower(text)
    elif args.title:
        text = title(text)
    print(text)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    main(args)