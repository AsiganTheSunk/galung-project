#!/usr/bin/python

from Metadata import Metadata
from Metadata import ExtendedMetada

class Node:
    def __init__(self, basename, identifier, metadata):
        self.identifier = identifier
        self.basename = basename
        self.parent_basename = None
        self.children = []
        self.metadata = metadata

    def set_children(self, children):
        self.children = children

    def get_children(self):
        return self.children

    def get_identifier(self):
        return self.identifier

    def set_basename(self, basename):
        self.basename = basename

    def set_parent_basename(self, parent_basename):
        self.parent_basename = parent_basename

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child_basename):
        new_child_list = []
        for item in self.children:
            if item.basename != child_basename:
                new_child_list.append(item)
        self.set_children(new_child_list)
        return self.children

    def get_metadata(self):
        return self.metadata

