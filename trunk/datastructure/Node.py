#!/usr/bin/python

from Metadata import Metadata
from Metadata import ExtendedMetada

class Node:
    def __init__(self, basename, identifier):
        self.identifier = identifier
        self.basename = basename
        self.parent_basename = None
        self.children = []
        self.metada = Metadata()

    def get_identifier(self):
        return self.identifier

    def set_basename(self, basename):
        self.basename = basename

    def set_parent_basename(self, parent_basename):
        self.parent_basename = parent_basename

    def add_child(self, child):
        self.children.append(child)

    def get_metadata(self):
        return self.metada

