#!/usr/bin/python

from trunk.filemapper import filemapper as fm
from trunk.filemapper import retrieve_module as rmod
from trunk.filemapper import check_module as cmod
import os
from time import sleep
from tqdm import tqdm
import pandas as pd
from pandas import DataFrame, Series
import tvdb_api
import numpy as np
import re
from trunk.datastructure.Metadata import Metadata
from trunk.datastructure.TreeRoot import TreeRoot
from trunk.ffmpeg.configuration import create_config_dir
from trunk.ffmpeg.configuration import read_config

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

basedir = str(os.getcwd())+'/testlibrary'

def create_data_frame (tree):
    basenamelist = []
    identifierlist = []
    parent_basenamelist = []

    namelist = []
    seasonlist = []
    episodelist = []
    fflaglist = []

    for node in tree.nodes:
        metadata = node.get_metadata()
        identifierlist.append(node.identifier)
        basenamelist.append(node.basename)
        parent_basenamelist.append(node.parent_basename)

        namelist.append(metadata.get_name())
        episodelist.append(metadata.get_episode())
        seasonlist.append(metadata.get_season())
        fflaglist.append(metadata.get_file_flag())

    episodelist = clean_integer_data(episodelist)
    seasonlist = clean_integer_data(seasonlist)

    dict = {'name':namelist,
            'season':seasonlist,
            'episode':episodelist,
            'fflag':fflaglist,
            'basename':basenamelist,
            'parent':parent_basenamelist
            }

    print DataFrame(dict)
    return DataFrame(dict)

def clean_integer_data(list):
    for i in range(0, len(list), 1):
        if list[i] == '':
            list[i] = 'N/A'
        else:
            list[i] = str(int(list[i]))
    return list


def retrieve_name_series (dataframe):
    unique_series = dataframe.name.unique()
    return unique_series[1:]


def retrieve_season_count(dataframe, current_serie):
    dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
    total_seasons = rmod.retrieve_number_of_seasons(current_serie)
    current_seasons = len(dataframe_episodes.season.unique())
    season_str = '### Seasons Found ({current}/{total})'.format(current=current_seasons, total=total_seasons)
    print season_str
    return total_seasons


def retrieve_episodes_count(dataframe, current_serie,  fflag=None):
    dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
    dataframe_episodes_of_season = dataframe_episodes[dataframe_episodes.fflag == '3']
    dataframe_seasons = dataframe_episodes[dataframe_episodes.fflag == '2']

    print 'Current Show Episode Files'
    print dataframe_episodes_of_season
    if len(dataframe_seasons != 0):
        print 'Current Show Season Directories'
        print dataframe_seasons
        print
    return [dataframe_seasons, dataframe_episodes_of_season]


def retrieve_episodes_found(dataframe, current_serie):
    dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
    dataframe_episodes_of_season = dataframe_episodes[dataframe_episodes.fflag == '3']
    dataframe_seasons = dataframe_episodes[dataframe_episodes.fflag == '2']
    total_seasons = rmod.retrieve_number_of_seasons(current_serie)
    for i in range(0, total_seasons, 1):
        try:
            total_episodes = rmod.retrieve_number_of_episodes_per_season(current_serie, i)
            current_episodes = len(dataframe_episodes_of_season[dataframe_episodes_of_season.season == str(i)])
        except:
            continue
        else:
            if current_episodes > 0:
                print ('### Season {season} Episodes Found ({current}/{total})').format(season=i, current=current_episodes, total=total_episodes)
                basename = dataframe_seasons.basename[dataframe_seasons.season == str(i)]
                key = 'New Season Directory [Season Y]'
                if len(basename) == 0:
                    print 'New Season Directory [Season Y]'
                for value in basename:
                    print 'Out: '+ str(value)
                    key = value

                dataframe_episodes_of_season.loc[dataframe_episodes_of_season.season == str(i), 'parent'] = str(key)

    print dataframe_episodes_of_season
    return


def retrieve_statistics(dataframe):
    unique_series = retrieve_name_series(dataframe)
    print ('\n### Number Of Series Detected ({current}) ###').format(current=len(unique_series))
    for current_serie in unique_series:
        print ('### Serie Name: {current}').format(current=current_serie)
        retrieve_season_count(dataframe=dataframe, current_serie=current_serie)
        retrieve_episodes_count(dataframe, current_serie=current_serie)
        retrieve_episodes_found(dataframe=dataframe, current_serie=current_serie)

def file_mapper():
    print (' ' + '------' * 20)
    print ('|' + '\t' * 6 + 'FILE_MAPPER' +'\t'*8 + ' |')
    print (' ' + '------' * 20 + '\n')
    directory = fm.directory_mapper(path=basedir, verbose=False)
    trees = fm.build_directory_tree (basedir=basedir, directory=directory, verbose=False, debug=False , deep=False)
    dataframe = create_data_frame (trees[0])

    retrieve_name_series(dataframe)
    retrieve_statistics(dataframe)


def main():
    file_mapper()


if __name__ == '__main__':
    main()

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
