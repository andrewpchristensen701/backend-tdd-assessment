#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here


def test_upper(self):
    parser = echo.create_parser()
    args = parser.parse_args(['-u', 'howdy'])
    print(args)
    result = echo.upper("howdy".upper())
    self.assertEquals(result, "HOWDY")
    self.assertEquals(args.upper, True)


def test_lower(self):
    parser = echo.create_parser()
    args = parser.parse_args(['-l', 'howdy'])
    print(args)
    result = echo.lower("howdy".lower())
    self.assertEquals(result, "howdy")
    self.assertEquals(args.lower, True)


def test_title(self):
    parser = echo.create_parser()
    args = parser.parse_args(['-t', 'Howdy'])
    print(args)
    result = echo.title("Howdy".title())
    self.assertEquals(result, "Howdy")
    self.assertEquals(args.title, True)


if __name__ == '__main__':
    unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
