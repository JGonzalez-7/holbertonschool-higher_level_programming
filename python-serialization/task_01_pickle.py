#!/usr/bin/env python3
"""
Pickling custom classes with exception handling.

- CustomObject.serialize(): saves the instance to a pickle file
- CustomObject.deserialize(): loads an instance from a pickle file

If the file does not exist or is malformed, methods return None.
"""

import pickle


class CustomObject:
    """A simple custom object that can be pickled/unpickled."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize (pickle) the current instance to a file.

        Args:
            filename (str): path to the output .pkl file

        Returns:
            None (always). If an error occurs, returns None as well.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PicklingError):
            return None
        return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize (unpickle) an instance from a file.

        Args:
            filename (str): path to the input .pkl file

        Returns:
            CustomObject instance on success, or None on failure.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if not isinstance(obj, cls):
                return None
            return obj
        except (FileNotFoundError, OSError, EOFError,
                pickle.UnpicklingError, AttributeError, ValueError):
            return None
