#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import echo
import subprocess


# Your test case class goes here
"""Created by ZacharyKline with help from Peter to finish
    off the finite details"""


class TestEcho(unittest.TestCase):
    def test_upper(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-u', 'hello'])
        print(args)
        result = echo.upper('hello'.upper())
        self.assertEquals(result, 'HELLO')
        self.assertEquals(args.upper, True)

    def test_lower(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-l', 'hello'])
        print(args)
        result = echo.lower('HELLO'.lower())
        self.assertEquals(result, 'hello')
        self.assertEquals(args.lower, True)

    def test_title(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-t', 'hello'])
        print(args)
        result = echo.title('hello'.title())
        self.assertEquals(result, 'Hello')
        self.assertAlmostEquals(args.title, True)

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def text_all(self):
        result = echo.upper('hello')
        result = echo.lower(result)
        result = echo.title(result)

        self.assertEquals(result, 'Hello')

    def text_none(self):
        parser = echo.create_parser()
        args = parser.parse_args(['hello'])
        result = echo.main(args)
        self.assertEquals(result, 'hello')


if __name__ == '__main__':
    unittest.main()