#!/usr/bin/python


class Library:
    def __init__(self):
        self.libray_list = []


    def add_library_source(self, path=None):
        return self.libray_list.append(path)


    def remove_library_source(self, path=None):
        return self.libray_list.remove(path)


    def list_library_source(self):
        for i in self.library_list:
            print (self.library_list[i])