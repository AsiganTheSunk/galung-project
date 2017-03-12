#!/usr/bin/python
#-*- coding. utf-8 -*-

from main.filemapper import filemapper as fm
from main.filemapper.pandas import pandas_module as pmod
import os

def filemapper_cc():
    print(' ' + '------' * 20)
    print('|' + '\t' * 6 + 'FILE_MAPPER_CC' + '\t'*8 + ' |')
    print(' ' + '------' * 20 + '\n')
    library = raw_input("[ library path: ]: ")

    if not os.path.exists(library):
        print('Invalid Path')
        return
    directory = fm.directory_mapper(path=library, verbose=False)
    trees = fm.build_directory_tree(basedir=library, directory=directory, verbose=False, debug=False , deep=False)

    print('\n' + '________' * 20)
    dataframe = pmod.create_data_frame(tree=trees[0])
    old_dataframe = dataframe

    dataframe = pmod.create_library(dataframe=dataframe, library=os.path.basename(library))

    print('\n--: Dataframe Original:')
    print(' ' + '------' * 20)
    print(dataframe)
    print(' ' + '------' * 20)

    tree = pmod.update_tree_info(old_dataframe=old_dataframe, dataframe=dataframe, tree=trees[0])

    print('\n--: Dataframe Final:')
    print(' ' + '------' * 20)
    tree.tree()
    print(' ' + '------' * 20)

    print('\n--: Library Statistics')
    pmod.retrieve_library_show_statistics(dataframe=dataframe)

    print('Applying Changes')
    fm.library_goes_live(old_tree=trees[1], new_tree=tree, library=library)

def main():
    filemapper_cc()

if  __name__ == '__main__':
    main()
