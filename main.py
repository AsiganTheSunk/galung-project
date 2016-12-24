#!/usr/bin/python

from trunk.filemapper import filemapper as fm
from trunk.filemapper import retrieve_module as rmod
from trunk.filemapper import check_module as cmod
import os
from time import sleep
from tqdm import tqdm
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import re
from trunk.datastructure.Metadata import Metadata
from trunk.datastructure.TreeRoot import TreeRoot
from trunk.ffmpeg.configuration import create_config_dir
from trunk.ffmpeg.configuration import read_config

basedir = str(os.getcwd())+'/testlibrary'

def run():
    print (' ' + '------' * 20)
    print ('|' + '\t' * 6 + 'FILE_MAPPER' +'\t'*8 + ' |')
    print (' ' + '------' * 20 + '\n')
    directory = fm.directory_mapper(path=basedir, verbose=False)
    trees = fm.build_directory_tree (basedir=basedir, directory=directory, verbose=False, debug=False , deep=False)
    print

    #trees[0].display()

    identifierlist = []
    basenamelist = []
    parent_basenamelist = []

    namelist = []
    seasonlist = []
    episodelist = []

    for item in trees[1].nodes:
        identifierlist.append(item.identifier)
        basenamelist.append(item.basename)
        parent_basenamelist.append(item.parent_basename)
        metadata = item.get_metadata()
        namelist.append(metadata.get_name())
        episodelist.append(metadata.get_episode())
        seasonlist.append(metadata.get_season())

    # dict = {'identifier':identifierlist, 'basename':basenamelist, 'parent_basename':parent_basenamelist}
    dict2 = {'name':namelist,'season':seasonlist, 'episode':episodelist}
    df = DataFrame(dict2)
    print df

    # todo recuperar files en base al flag, despues aplicar unique, recuperamos los nombre unicos de la series
    series = df.name.unique()
    series_str = '### Number Of Series Detected ({series}) ###'.format(series=(len(series) - 1))
    print series_str

    for serie in series[1:]:
        serie_str = '### -{serie}'.format(serie=serie)
        print serie_str

    t = dict(list(df.groupby('name')))
    print t
    for cap in t:
        if cap not in '':
            cap_str = '### Number Of Capitules -{cap}'.format(cap=cap)
            # todo por nombre recupera el numero de seasons en total, con esta info podemos hacer alguna cosilla

    for cap in t:
        cap_str = '### Seasons Of Capitules -{cap}'.format(cap=cap)








def main():
    run()
    # run()
    # path = '/home/asigan/TFG/mozart.str'
    # coco = rmod.retrieve_str_language(path=path)


if __name__ == '__main__':
    main()
