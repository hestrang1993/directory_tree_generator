"""
cli provides the command line interface (CLI) for the Directory Tree Generator.
"""

import argparse
import pathlib
import sys

from . import __version__
from .directory_tree import DirectoryTree


parser = argparse.ArgumentParser(
    prog="tree",
    description="Directory Tree Generator helps generate directory trees for a given directory.",
    epilog="Thank you for using the Directory Tree Generator."
)
"""
argparse.ArgumentParser: The object for parsing command line strings into Python objects.
"""
parser.version = f"Directory Tree Version: v{__version__}"
parser.add_argument("-v", "--version", action="version")
parser.add_argument(
    "root_dir",
    metavar="ROOT_DIR",
    nargs="?",
    default=".",
    help="Generate a full directory tree starting at ROOT_DIR",
)


def main():
    """
    main calls parse_cmd_line_arguments() and pack the command line arguments in args.

    It then turn the root directory into a pathlib.Path object.
    Finally, create a DirectoryTree object using root_dir as an argument and call .generate() on it to generate and display the corresponding directory tree diagram on your terminal window.

    Returns
    -------
    None
    """
    args = parser.parse_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(root_dir)
    tree.generate()
