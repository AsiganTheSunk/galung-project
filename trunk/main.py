#!/usr/bin/python

from trunk.filemapper import filemapper as fm
import os

basedir = str(os.getcwd())+'/testlibrary'

def main():
    directory = fm.directory_mapper(path= basedir)
    fm.build_directory_tree (basedir=basedir, directory=directory, verbose=True)

if __name__ == '__main__':
    main()
