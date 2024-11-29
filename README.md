# dotfile_mgr

*(Still in development)*

Shared user setup configuration for Linux and Mac

I got tired of having to rebuild my basic environment every time I
setup a new Mac or Linux machine. So I automated it.

If you find this useful too, please provide some feedback to make it better!

## Basics
The files are stored without dots to hide them.

A simple script (written in Python) exists to do the simple refresh steps.

The idea is to replace files like `.bashrc` and `.zshrc` with links
to a checked-out Git workspace that can easily be updated.

## Managed files

- `~/.bashrc`
- `~/.profile`
- `~/.zshrc`
- `~/.local/bin/**` (partial)

## Use at your own risk
This approach works well for me but there are some cautions:

- Don't delete or move your workspace when actual dotfiles are symlinks!
- Some installations manipulate these files.
