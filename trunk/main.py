#!/usr/bin/python

import os
import re
import pandas as pd
import shutil
from trunk.filemapper import filemapper as fm
from trunk.pandas import pandas_module as pmod
from trunk.datastructure.TreeRoot import TreeRoot

basedir = str(os.getcwd()) + '/testlibrary'

def file_mapper():
    print(' ' + '------' * 20)
    print('|' + '\t' * 6 + 'FILE_MAPPER' + '\t'*8 + ' |')
    print(' ' + '------' * 20 + '\n')
    directory = fm.directory_mapper(path=basedir, verbose=False)
    trees = fm.build_directory_tree(basedir=basedir, directory=directory, verbose=False, debug=False , deep=False)
    trees[0].display()

    print('\n' + '________' * 20)
    dataframe = pmod.create_data_frame(tree=trees[0])
    temp = dataframe
    #pmod.retrieve_library_show_statistics(dataframe=dataframe)
    dataframe = pmod.create_library(dataframe=dataframe, library='testlibrary')
    #pmod.retrieve_library_show_statistics(dataframe=dataframe)
    print('\n Dataframe Original:')
    print(' ' + '------' * 20)
    print(dataframe)
    print(' ' + '------' * 20)
    tree = pmod.update_tree_info(old_dataframe=temp, dataframe=dataframe, tree=trees[0])
    print('\n Dataframe Final:')
    print(' ' + '------' * 20)
    tree.tree('testlibrary')
    print(' ' + '------' * 20)

    l = tree.build_full_path_tree()
    l2 = trees[1].build_full_path_tree()

    # tree.tree_path()
    # print(' ' + '------' * 20)
    # trees[1].tree_path()

    # print
    # print 'number of elements: ' +str(len(l))
    # print 'number of new elements: ' +str(len(l)-len(l2))
    # print 'number of old elements: ' +str(len(l2))

    basedir2 = os.getcwd()
    list_index_files = []
    list_index_dir = []


    for index in range(1, len(l2), 1):
        current_item = basedir2 + l2[index]
        if os.path.isfile(unicode(current_item)):
            list_index_files.append(index)

        if os.path.isdir(unicode(current_item)):
            list_index_dir.append(index)


    for index in range(len(l2), len(l), 1):
        new_file = basedir2 + '/result' + l[index]
        if not os.path.exists(new_file):
            os.makedirs(new_file)

    for index in list_index_dir:
        new_file = basedir2 + '/result' +l[index]
        if not os.path.exists(new_file):
            os.makedirs(new_file)

    for index in list_index_files:
        new_file = basedir2 + '/result' + l[index]
        old_file = basedir2 + l2[index]
        try:
            os.rename(old_file, new_file)
        except Exception as e:
            print 'Error Moving File {current_file}, {error}'.format(current_file=old_file, error=str(e))

    old_library = basedir2 + '/testlibrary'
    try:
        shutil.rmtree(old_library, ignore_errors=True)
        os.rename(basedir2 + '/result'+'/testlibrary', basedir2+'/testlibrary')
        shutil.rmtree(basedir2 + '/result', ignore_errors=True)
    except Exception as e:
        print e


def tree_test_update():
    tree = TreeRoot()
    tree.add_node(basename='library')
    tree.add_node(basename='capituloa', parent_basename='library')
    tree.add_node(basename='capituloa.mkv', parent_basename='capituloa')
    tree.add_node(basename='seasonx', parent_basename='library')
    tree.add_node(basename='capituloz.mkv', parent_basename='seasonx')
    tree.display()
    tree.tree(basename='library')
    #tree.subtree(basename='capituloa', parent_basename='library')
    #tree.update_parent_node_byindex()

    #tree.add_node_byindex('capitulob', parent='seasonx', parent_index=None, debug=True)
    tree.update_parent_node_byindex(1, 'seasonx')
    tree.display()

    tree.tree(basename='library')
    tree.add_node(basename='seriea',parent_basename='library')
    tree.update_parent_node_byindex(3, 'seriea')
    tree.add_node(basename='capitulob', parent_basename='seasonx')


    tree.tree(basename='library')
def main():
    file_mapper()
    #tree_test_update()

if __name__ == '__main__':
    main()


# todo cambios que tengo que hacer, ha de aplicarse al dataframe, no a un subconjunto.
# todo renombrar padres de las carpetas
# todo si el fichero no tiene carpeta, crearsela
# todo modificar la tabla final usando los propios indices del dataframe como referencia de la linea a modificar
# todo anadir las entradas necesarias, tener en cuenta que el momento que se detecta la serie, se genera el
# todo el directorio de la misma, osea se ha de anadir una nueva fila

# todo aplicar los cambios
# todo validar los cambios

# todo aplicar el filtro de file flag antes!!!
# todo al haberlo mapeado de la manera que lo hicimos, sorted(dict) el Dataframe se mapaea igual que los nodos, 0
# todo no existe, comienza en el 1 al igual que los node_identifier, aprovechamos esto, para decirle, al arbol
# todo que nuevos nodos han de ser creados y modificados.

# todo crear el directorio de la serie si no existe en la ruta de la libreria
# todo crear el directorio_season

# todo para actualizar el arbol, en base al index recupear el nodo y su padre, quitar el nodo de la lista del padre
# todo anadirselo al nuevo padre y modificiar el valor de parent_basename al nuevo nombre
# todo una vez estemos en esta situacion, os.rename(trees[0].gefullpath(dir), trees[0].getfullpath(dir))

# todo frames = [df1, df2, df3]
# todo df['col2'] = df.apply(lambda x: x['col1'] if x['col1'] in l else None, axis=1)
