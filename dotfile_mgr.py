#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Copyright (c) 2024 by Mike Geipel
# MIT License: https://github.com/geipel/dotfiles/blob/main/LICENSE
# =============================================================================

"""
A simple command line interface for managing dotfiles.

This app should rely only on built-in Python libraries,
so it can be used as a standalone script.
"""

import cmd


class DotMgr(cmd.Cmd):
    """ Simple command line interface for managing dotfiles. """
    prompt = '>> '
    intro = "Welcome to Dotfile Manager. Type help or ? to list"

    def do_exit(self, line: str):
        """ Exit the program. """
        print(f"Exiting... {line}")
        return True

    def do_greet(self, line: str):
        """ Greet the user. """
        print(f"Hello, {line.strip() or 'world'}!")


if __name__ == '__main__':
    DotMgr().cmdloop()
    exit(0)

from pytest import CaptureFixture


class TestDotMgr:  # pylint: disable=missing-function-docstring
    """ Test the DotMgr class. """

    def test_do_exit(self):
        assert DotMgr().do_exit("") is True

    def test_do_greet_with_name(self, capsys: CaptureFixture):
        DotMgr().do_greet("Python")
        captured = capsys.readouterr()
        assert captured.out == "Hello, Python!\n"

    def test_do_greet_empty(self, capsys: CaptureFixture):
        DotMgr().do_greet("")
        captured = capsys.readouterr()
        assert captured.out == "Hello, world!\n"
