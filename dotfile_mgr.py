#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Copyright (c) 2024 by Mike Geipel
# MIT License: https://github.com/geipel/dotfile_mgr/blob/main/LICENSE
# =============================================================================

"""
A simple command line interface for managing dotfiles.

This app should rely only on built-in Python libraries,
so it can be used as a standalone script.

(However, unit tests are currently still inline; pytest is needed to run them.)
"""

import cmd
from pathlib import Path
import sys


class DotMgr(cmd.Cmd):
    """ Simple command line interface for managing dotfiles. """
    prompt = '>> '
    intro = "Welcome to Dotfile Manager. Type help or ? to list"
    dst_dir = Path.home()
    bld_dir = Path(__file__).resolve().parent / "build"
    src_dir = Path(__file__).resolve().parent / "dotfiles"

    def do_exit(self, line: str):
        """ Exit the program. """
        print(f"Exiting... {line}")
        return True

    def do_greet(self, line: str):
        """ Greet the user. """
        print(f"Hello, {line.strip() or 'world'}!")


if __name__ == '__main__':
    DotMgr().cmdloop()
    sys.exit(0)

# For simplicity: unit tests follow, for now.
# They should be separated into separate folder.
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

    def test_home_dir(self):
        assert Path.home() == DotMgr().dst_dir

    def test_build_dir(self):
        assert Path.cwd() / "build" == DotMgr().bld_dir

    def test_file_dir(self):
        assert Path.cwd() / "dotfiles" == DotMgr().src_dir
