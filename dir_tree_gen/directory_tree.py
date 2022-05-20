"""directory_tree provides the main module for the Directory Tree Generator."""
import sys
from .tree_generator import TreeGenerator


class DirectoryTree:
    """DirectoryTree is a high-level class to create the directory tree diagram and display it on your screen."""

    def __init__(self, root_dir, dir_only=False, output_file=sys.stdout):
        """
        __init__ creates a new DirectoryTree instance.

        Parameters
        ----------
        root_dir : str
            The absolute path to the root directory.
        dir_only: bool
            A flag to generate and display directory-only tree diagrams (True) or not (False).
        output_file: _io.TextIOWrapper

        """
        self._output_file = output_file
        self._generator = TreeGenerator(root_dir, dir_only)

    def generate(self):
        """
        generate creates and prints out a directory tree.

        Returns
        -------
        None
        """
        tree = self._generator.build_tree()
        if self._output_file != sys.stdout:
            # Wrap the tree in a Markdown code block.
            tree.insert(0, "```")
            tree.append("```")
            self._output_file = open(self._output_file, mode="w", encoding="UTF-8")
        with self._output_file as stream:
            for entry in tree:
                print(entry, file=stream)
