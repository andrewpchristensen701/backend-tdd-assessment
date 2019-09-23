#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here


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

        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_all(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-tul', 'hello'])
        print(args)
        string = "hello"
        result = echo.lower(echo.upper(echo.title(string)))
        self.assertEquals(result, "hello")
        self.assertEquals(args.upper, True)
        self.assertEquals(args.lower, True)
        self.assertEquals(args.title, True)




if __name__ == '__main__':
    unittest.main()