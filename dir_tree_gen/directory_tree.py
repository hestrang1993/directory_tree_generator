"""directory_tree provides the main module for the Directory Tree Generator."""

from .tree_generator import TreeGenerator


class DirectoryTree:
    """DirectoryTree is a high-level class to create the directory tree diagram and display it on your screen."""

    def __init__(self, root_dir):
        """
        __init__ creates a new DirectoryTree instance.

        Parameters
        ----------
        root_dir : str
            The absolute path to the root directory.
        """
        self._generator = TreeGenerator(root_dir)

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
