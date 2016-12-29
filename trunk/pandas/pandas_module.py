#!/usr/bin/python

import re
import os
import pandas as pd
from pandas import DataFrame

from trunk.datastructure.Metadata import Metadata
from trunk.datastructure.TreeRoot import TreeRoot
from trunk.filemapper import filemapper as fm
from trunk.filemapper.retrieve import offline_retrieve_module as offrmod
from trunk.filemapper.retrieve import online_retrieve_module as onrmod

basedir = str(os.getcwd()) + '/testlibrary'
pd.set_option('display.max_rows', 750)
pd.set_option('display.max_columns',750)
pd.set_option('display.width', 1400)


def create_data_frame (tree=TreeRoot):
    basenamelist = []
    identifierlist = []
    parent_basenamelist = []
    namelist = []
    seasonlist = []
    episodelist = []
    fflaglist = []

    for node in tree.get_nodes():
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

    dict = {'name': namelist,
            'season': seasonlist,
            'episode': episodelist,
            'fflag': fflaglist,
            'basename': basenamelist,
            'parent': parent_basenamelist
            }

    dataframe = DataFrame(dict)
    print(dataframe)
    return dataframe


def clean_integer_data(list):
    for i in range(0, len(list), 1):
        if list[i] == '':
            list[i] = 'N/A'
        else:
            list[i] = str(int(list[i]))
    return list


def retrieve_name_series(dataframe):
    unique_series = dataframe.name.unique()
    return unique_series[1:]


def create_main_show_directory(dataframe, current_serie=str, library=str):
    try:
        #if not os.path.exists(os.path.join(basedir, current_serie)):
        #    os.makedirs(os.path.join(basedir, current_serie))
        print ('CREATED: ' + str(current_serie))
    except Exception as e:
        return dataframe
    else:
        dataframe = add_dataframe_row(dataframe=dataframe, name=current_serie, season='N/A', episode='N/A',
                                      fflag='15', basename=current_serie, parent=library)
    return dataframe


def create_season_directory(dataframe, current_serie=str, season=str, parent=str):
    try:
        new_season_directory = fm.build_season_directory_name(name=current_serie, season=str(season))
        #if not os.path.exists(os.path.join(basedir, new_season_directory)):
        #    os.makedirs(os.path.join(basedir, new_season_directory))
    except Exception as e:
        return dataframe
    else:
        print ('CREATED: ' + str(new_season_directory))
        dataframe = add_dataframe_row(dataframe=dataframe, name=current_serie, season=season, episode='N/A',
                                      fflag='2', basename=new_season_directory, parent=parent)
    return dataframe


def retrieve_episodes(dataframe, current_serie, drop_dup=False):
    if drop_dup:
        dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
    else:
        dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie)
    return dataframe_episodes[dataframe_episodes.fflag == '3']

def retrieve_episodes_directories(dataframe, current_serie, drop_dup=False):
    if drop_dup:
        dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
    else:
        dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie)
    return dataframe_episodes[dataframe_episodes.fflag == '1']


def retrieve_seasons(dataframe, current_serie, drop_dup=False):
    if drop_dup:
        dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
    else:
        dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie)
    return dataframe_episodes[dataframe_episodes.fflag == '2']


def retrieve_current_episodes_per_season (dataframe, current_serie):
    dataframe_episodes = retrieve_episodes(dataframe=dataframe, current_serie=current_serie)
    dataframe_episodes_directories = retrieve_episodes_directories(dataframe=dataframe, current_serie=current_serie)
    dataframe_seasons = retrieve_seasons(dataframe=dataframe, current_serie=current_serie)
    main_show_directory = dataframe[dataframe['basename'] == current_serie]
    current_status = 'NO'
    if not main_show_directory.empty:
        current_status = 'YES'
    print('------' * 20)
    print('-- Directory: {status} | SHOW NAME: {show_name} '.format(show_name=current_serie, status=current_status))
    print('------' * 20)

    try:
        total_seasons = onrmod.retrieve_number_of_seasons(current_serie)
        for i in range(0, total_seasons, 1):
            try:
                total_episodes = onrmod.retrieve_number_of_episodes_per_season(current_serie, i)
                dataframe_episodes_per_season = dataframe_episodes[dataframe_episodes.season == str(i)]
                current_episodes = len(dataframe_episodes_per_season)
            except:
                continue
            else:

                dataframe_season = dataframe_seasons[dataframe_seasons.season == str(i)]
                season_dir = 'NO '
                if not dataframe_season.empty:
                    season_dir = 'YES'
                print('Directory: {status} | Season {season} - Found ({current}/{total} Episodes)'.format(season=i, current=current_episodes, total=total_episodes, status=season_dir))
                dataframe_temp = dataframe_episodes_per_season.reindex()
                for index in range(0,len(dataframe_temp.index),1):
                    basename = dataframe_temp.iloc[int(index)]['basename']
                    dataframe_directory = dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]]
                    current_dir = 'NO '
                    if not dataframe_directory.empty:
                        current_dir = 'YES'
                    print('--: Directory: {status} | {basename}'.format(basename=basename,status=current_dir))
            print('------' * 20)

    except:
        return

def create_default_show_tree_directory(dataframe, current_serie=str, library=str, with_dir=True):
    main_show_directory = dataframe[dataframe['basename'] == current_serie]
    if main_show_directory.empty:
        print
        dataframe = create_main_show_directory(dataframe=dataframe, current_serie=current_serie, library=library)

    # retrieve season dataframe from current serie
    dataframe_seasons = retrieve_seasons(dataframe=dataframe, current_serie=current_serie)
    # retrieve episode file dataframe from current serie
    dataframe_episodes = retrieve_episodes(dataframe=dataframe, current_serie=current_serie)
    # retrieve episode directory dataframe from current serie
    dataframe_episodes_directories = retrieve_episodes_directories(dataframe=dataframe, current_serie=current_serie)

    # reset index to simply iterate over the rows, extracting the values, to create the directory tree
    dataframe_temp = dataframe_episodes.reindex()
    for index in range(0, len(dataframe_temp.index), 1):
        name = dataframe_temp.iloc[int(index)]['name']
        season = dataframe_temp.iloc[int(index)]['season']
        episode = dataframe_temp.iloc[int(index)]['episode']
        basename = dataframe_temp.iloc[int(index)]['basename']
        parent = dataframe_temp.iloc[int(index)]['parent']
        dataframe_season = dataframe_seasons[dataframe_seasons.season == season]
        if dataframe_season.empty:
            dataframe = create_season_directory(dataframe, current_serie=current_serie, season=season, parent=current_serie)
            # season_directory_name = fm.build_season_directory_name(name=current_serie,season=season)
            # dataframe = add_dataframe_row(dataframe=dataframe, name=name, season=season, episode='N/A', fflag='2', basename=season_directory_name, parent=current_serie)
        else:
            dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(dataframe_season.index), parent=current_serie)

        dataframe_directory = dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]]
        real_index = dataframe_episodes.index[dataframe_episodes.basename == basename]
        if dataframe_directory.empty:
            print('CREATED: ' + str(basename[:-4]))
            dataframe = add_dataframe_row(dataframe=dataframe, name=name, season=season, episode=episode, fflag='1', basename=basename[:-4], parent=parent)
            dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=basename[:-4])

    dataframe_temp = dataframe_episodes_directories.reindex()
    for index in range(0, len(dataframe_temp.index), 1):
        name = dataframe_temp.iloc[int(index)]['name']
        season = dataframe_temp.iloc[int(index)]['season']
        basename = dataframe_temp.iloc[int(index)]['basename']
        parent = dataframe_temp.iloc[int(index)]['parent']
        new_parent = fm.build_season_directory_name(name=name, season=season)
        real_index = dataframe_episodes_directories.index[dataframe_episodes_directories.basename == basename]
        if parent not in new_parent:
            dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=new_parent)
    return dataframe


def update_parent_dataframe_row (dataframe, index, parent):
    dataframe.loc[dataframe.index == index, 'parent'] = parent
    return dataframe


def retrieve_library_show_statistics(dataframe):
    unique_series = retrieve_name_series(dataframe=dataframe)
    print('------'*20)
    print('-- DETECTED [ {current} ] SHOWS'.format(current=len(unique_series)))
    for current_serie in unique_series:
        retrieve_current_episodes_per_season(dataframe=dataframe, current_serie=current_serie)
        print
    return dataframe


def create_library(dataframe, library=str):
    unique_series = retrieve_name_series(dataframe=dataframe)
    for current_serie in unique_series:
       dataframe = create_default_show_tree_directory(dataframe, current_serie=current_serie, library=library)

    return dataframe


def add_dataframe_row (dataframe, name, season, episode, fflag, basename, parent):
    dict = {'name' : [name],
            'season' : [season],
            'episode' : [episode],
            'fflag' : [fflag],
            'basename' : [basename],
            'parent' : [parent]
            }
    new_row = DataFrame(dict)
    dataframe = dataframe.append(new_row , ignore_index=True)
    return dataframe


def update_tree_info(old_dataframe, dataframe, tree):
    total_rows = len(dataframe.index)
    new_rows = total_rows - len(old_dataframe.index)
    print('--: New rows to be Added to the tree: ('+ str(new_rows) + '/' + str(total_rows) + ')')
    for index in range(len(old_dataframe.index), len(dataframe.index), 1):
        name = dataframe.iloc[int(index)]['name']
        season = dataframe.iloc[int(index)]['season']
        episode = dataframe.iloc[int(index)]['episode']
        basename = dataframe.iloc[int(index)]['basename']
        parent = dataframe.iloc[int(index)]['parent']
        # print('index: ' + str(index), 'basename: ' + str(basename),  'parent: ' + str(parent))
        # print('name: ' + str(name),'season: ' + str(season),'episode: ' + str(episode))
        metadata = Metadata()
        metadata.set_name(name)
        if season not in 'N/A':
            metadata.set_season(season)
        if episode not in 'N/A':
            metadata.set_episode(episode)
        tree.add_node(basename=basename, metadata=metadata, parent_basename=parent)

    print('--: Rows that need to be Updated in the tree: ('+ str(len(old_dataframe)) + '/' + str(total_rows) + ')')
    for index in range(0, len(old_dataframe.index), 1):
        current_basename = dataframe.iloc[int(index)]['basename']
        current_parent = dataframe.iloc[int(index)]['parent']
        node = tree.search(basename=current_basename)
        node = node[0]
        old_parent_basename = node.parent_basename
        if current_parent != old_parent_basename:
            #print('------'*20)
            #print('Input: index({index}) basename: {base} - [Parent]: old: {old_parent}'.format(index=index, old_parent=old_parent_basename, base=node.basename))
            #print('Onput: index({index}) basename: {basename} - [Parent]: new: {new_parent}'.format(index=index, basename=current_basename, new_parent=current_parent))
            tree.update_parent_node_byindex(index=int(index), parent=current_parent)

    return tree

