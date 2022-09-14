"""
tree_dict contains a dictionary that will enumerate all the various parts of a directory tree.
"""

_PIPE = "│"
"""str: A connection piece between the root directory and the rest of the tree."""
_ELBOW = "└──"
"""str: A connection piece between the terminal element in a directory and the tree branch/trunk."""
_TEE = "├──"
"""str: A connection piece between the current directory and its components."""
_PIPE_PREFIX = "│   "
"""
str: A connection piece that spaces out elements between sub-directories.
"""
_SPACE_PREFIX = "    "
"""
str: A blank element used for spacing.
"""

tree_dict = {
    "pipe": _PIPE,
    "elbow": _ELBOW,
    "tee": _TEE,
    "pipe prefix": _PIPE_PREFIX,
    "space prefix": _SPACE_PREFIX
}
"""
dict[str, str]: A dictionary listing all of the elements of a directory tree.

- pipe: "│"
- elbow: "└──"
- tee: "├──"
- pipe prefix: "│..."
- space prefix: "...."
"""
