"""directory_tree provides the main module for the Directory Tree Generator."""

from .tree_generator import TreeGenerator


class DirectoryTree:
    """DirectoryTree is a high-level class to create the directory tree diagram and display it on your screen."""

    def __init__(self, root_dir, dir_only=False):
        """
        __init__ creates a new DirectoryTree instance.

        Parameters
        ----------
        root_dir : str
            The absolute path to the root directory.
        dir_only: bool
            A flag to generate and display directory-only tree diagrams (True) or not (False).
        """
        self._generator = TreeGenerator(root_dir, dir_only)

    def generate(self):
        """
        Create and print out a directory tree.

        Returns
        -------
        None
        """
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)
