"""
_tree_generator holds the components (branches, roots, pipes, tees, etc.) of the directory tree and the class that creates the blueprint for the tree.
"""

import os
import pathlib

from dir_tree_gen.tree_dict import tree_dict


class TreeGenerator:
    """_TreeGenerator traverses the file system and generates the directory tree diagram."""

    def __init__(self, root_dir, dir_only=False):
        """
        __init__ creates a new _TreeGenerator instance.

        Parameters
        ----------
        root_dir : str
            The absolute path to the root directory.
        dir_only: bool
            A flag to generate and display directory-only tree diagrams (True) or not (False).
        """
        self._root_dir = pathlib.Path(root_dir)
        """pathlib.Path: The root directory"""
        self._dir_only = dir_only
        """bool: A flag to generate and display directory-only tree diagrams (True) or not (False)"""
        self._tree = []
        """list: A list to store the entries that shape the directory tree diagram"""

    def build_tree(self):
        """
        Generate and return the directory tree diagram.

        Returns
        -------
        list
            A list to store the entries that shape the directory tree diagram.
        """
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        """
        _tree_head builds the head of the directory tree.

        Returns
        -------
        None
        """
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(tree_dict["pipe"])

    def _tree_body(self, directory, prefix=""):
        """
        _tree_body builds the body of the directory tree.

        This method first iterates over a given directory.
        This method then sorts the entries into files and subdirectories.
        This method counts the number of entries.
        Each entry in the directory is then enumerated.

        Parameters
        ----------
        directory : pathlib.Path
            The path to the directory you want to walk through.
        prefix : str
            A prefix string that is used to draw the tree diagram on the terminal window.

            This string helps to show up the position of the directory or file in the file system.

        Returns
        -------
        None
        """
        entries = self._prepare_entries(directory)
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = tree_dict["elbow"] if index == entries_count - 1 else tree_dict["tee"]
            self._check_if_dir(entry, index, entries_count, prefix, connector)

    def _prepare_entries(self, directory):
        """
        _prepare_entries prepares the directory entries to generate either a full tree or a directory-only tree.

        Parameters
        ----------
        directory : pathlib.Path
            The path to the directory you want to walk through.

        Returns
        -------
        list
            A list of entries in the directory.
        """
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries

    def _check_if_dir(self, entry, index, entries_count, prefix, connector):
        """
        _check_if_dir checks if the current entry is a directory.

        If so, then the if code block calls ._add_directory() to add a new directory entry.
        Otherwise, the else clause calls ._add_file() to add a new file entry.

        Parameters
        ----------
        entry : pathlib.Path
            A filesystem path.
        index : int
            The index of a particular entry.
        entries_count : int
            The total number of entries.
        prefix : str
            A prefix string that is used to draw the tree diagram on the terminal window.
        connector : str
            The connecting piece that will attach the entry to the tree.

        Returns
        -------
        None
        """
        if entry.is_dir():
            self._add_directory(entry, index, entries_count, prefix, connector)
        else:
            self._add_file(entry, prefix, connector)

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        """
        _add_directory adds a subdirectory to the tree diagram.

        Parameters
        ----------
        directory : pathlib.Path
            A subdirectory within the root directory.
        index : int
            The index of a particular entry.
        entries_count : int
            The total number of entries.
        prefix : str
            A prefix string that is used to draw the tree diagram on the terminal window.
        connector : str
            The connecting piece that will attach the entry to the tree.

        Returns
        -------
        None
        """
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        self._update_prefix_by_entry_index(directory, index, entries_count, prefix)

    def _update_prefix_by_entry_index(self, directory, index, entries_count, prefix):
        """
        _update_prefix_by_entry_index runs a conditional statement that updates ``prefix`` according to the ``index`` of the current entry.

        Parameters
        ----------
        directory : pathlib.Path
            A subdirectory within the root directory.
        index : int
            The index of a particular entry.
        entries_count : int
            The total number of entries.
        prefix : str
            A prefix string that is used to draw the tree diagram on the terminal window.

        Returns
        -------
        None
        """
        if index != entries_count - 1:
            prefix += tree_dict["pipe prefix"]
        else:
            prefix += tree_dict["space prefix"]
        self._tree_body(
            directory=directory,
            prefix=prefix
        )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        """
        _add_file appends a file entry to the directory tree list.

        Parameters
        ----------
        prefix : str
            A prefix string that is used to draw the tree diagram on the terminal window.
        connector : str
            The connecting piece that will attach the entry to the tree.

        Returns
        -------
        None
        """
        self._tree.append(f"{prefix}{connector} {file.name}")
