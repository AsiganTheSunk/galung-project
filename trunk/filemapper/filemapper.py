#!/usr/bin/python

import os
from logging import DEBUG
from logging import basicConfig
from logging import debug as log_debug
from time import sleep

from enum import Enum
from tqdm import tqdm

import trunk.filemapper.check.check_module as cmod
import trunk.filemapper.retrieve.offline_retrieve_module as offrmod
import trunk.filemapper.retrieve.online_retrieve_module as onrmod
from trunk.datastructure.Metadata import Metadata
from trunk.datastructure.TreeRoot import TreeRoot


# todo FLAGS: to be moved to somewhere else. anadir las que faltan!!!!!!!!!!!
# todo FileMapper: validation

class FLAGS(Enum):
    LIBRARY_DIRECTORY_FLAG = '0'  # Library
    SHOW_DIRECTORY_FLAG = '1'  # Directory
    SEASON_DIRECTORY_FLAG = '2'  # Season show directory
    SHOW_FLAG = '3'  # Multimedia file (.mkv, .mp4):
    SUBTITLE_DIRECTORY_FLAG = '4'  # Subtitle directory
    SUBTITLE_FLAG = '5'  # Subtitle file (.str, .sub): files to be inyected with?
    FILM_DIRECTORY_FLAG = '6'  # Film directory
    FILM_FLAG = '7'  # Multimedia file (.mk, .mp4):
    UNKOWN_FLAG = '8'  # Unkown File Type:
    TRASH_FLAG = '9'  # Unwanted File
    ANIME_DIRECTORY_FLAG = '10'
    ANIME_FLAG = '11'

directory_dict = {}
tOriginal = TreeRoot()
tUpdated = TreeRoot()
basicConfig(filename=str(os.getcwd() + '/trunk/log/test.log'), filemode='w', format='%(filename)s %(message)s', level=DEBUG)


def directory_mapper(path=None, verbose=None):
    item_count = 1
    for root, directories, files in os.walk(path):
        item_count += len(directories)

    for root, directories, files in os.walk(path):
    #for root, directories, files in tqdm(os.walk(path), total=item_count, desc='Mapping Folder', ncols=115, unit=' items'):
        sleep(0.04)
        for directory in directories:
            try:
                if cmod.check_subtitles_directory(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.SUBTITLE_DIRECTORY_FLAG
                elif cmod.check_show_directory(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.SHOW_DIRECTORY_FLAG
                elif cmod.check_season_directory(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.SEASON_DIRECTORY_FLAG
                elif cmod.check_film_type(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.FILM_DIRECTORY_FLAG
                elif cmod.check_anime_dir(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.ANIME_DIRECTORY_FLAG
            except Exception as e:
                continue

        for file_ in files:
            try:
                if cmod.check_subtitles(file_):
                    directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = FLAGS.SUBTITLE_FLAG
                elif cmod.check_unwanted(file_):
                    directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = FLAGS.TRASH_FLAG
                elif cmod.check_season(file_):
                    directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = FLAGS.SHOW_FLAG
                elif cmod.check_film_type(file_):
                    directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = FLAGS.FILM_FLAG
                elif cmod.check_anime_show(file_):
                    directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = FLAGS.ANIME_FLAG
            except Exception as e:
                continue

    list_directory(directory_dict)
    return directory_dict


def build_directory_tree(basedir=None, directory=None, verbose=None, debug=None, deep=None):
    try:
        item_count = len(directory)
        tOriginal.add_node(basename=str(os.path.basename(basedir)))
        tUpdated.add_node(basename=str(os.path.basename(basedir)))

        #for item in tqdm(sorted(directory), total=item_count, desc='Building Tree ', ncols=115, unit=' items'):
        for item in sorted(directory):
            len_aux = len(str(os.path.basename(item)))
            parent = item[:-len_aux - 1]
            metadata = retrieve_show_info(path=str(item), verbose=verbose, file_flag=directory[item], deep=deep, debug=debug)
            new_basename = rebuild_name(meta=metadata, verbose=verbose)

            if parent in basedir:
                parent_metadata = retrieve_show_info(path=str(parent), verbose=verbose, file_flag=FLAGS.LIBRARY_DIRECTORY_FLAG, deep=deep, debug=debug)
                new_parent_basename = rebuild_name(meta=parent_metadata, verbose=verbose)
            else:
                parent_metadata = retrieve_show_info(path=str(parent), verbose=verbose, file_flag=directory[parent], deep=deep, debug=debug)
                new_parent_basename = rebuild_name(meta=parent_metadata, verbose=verbose)

            tOriginal.add_node(basename=str(os.path.basename(item)), metadata=metadata, parent_basename=str(os.path.basename(parent)))
            tUpdated.add_node(basename=str(new_basename), metadata=metadata, parent_basename=str(new_parent_basename))

            message = 'Tree: item_flag: ' + str(directory[item]), 'Iitem: ' + str(os.path.basename(item)), 'Iparent: ' + str(os.path.basename(parent))
            log_debug(message)
            message = 'Tree: item_flag: ' + str(directory[item]), 'Oitem: ' + str(new_basename), 'Oparent: ' + str(new_parent_basename)
            log_debug(message)

    except Exception as e:
        print (str('build-directory-tree: ') + str(e))
    else:
        return [tUpdated, tOriginal]


def list_directory(dict):
    for item in sorted(dict):
        message = 'item_flag: ' + dict[item], 'path: ' + item
        log_debug(message)


def rename(path=None, new_path=None):
    try:
        os.rename(path, new_path)
    except Exception as e:
        return
    else:
        return


def prettify_title(path=None):
    try:
        new_path = path.replace('-', ' ').replace('.', ' ').replace('_', ' ').rstrip().title()
    except Exception as e:
        return path
    else:
        return new_path


# todo con eso el mapeo esta finalizado, solo falta usar el objeto de Metadatos para almacenar la info
def retrieve_show_info(path=None, verbose=None, file_flag=None, deep=None, debug=None):
    metadata = Metadata()
    film_flag = year = ''
    name = season = episode = ename = ''
    subtitle = audio = codec = uploader = source = ''
    language = ''
    try:
        aux = str(os.path.basename(path))
        if int(file_flag) == int(FLAGS.LIBRARY_DIRECTORY_FLAG):
            name = aux
        elif int(file_flag) == int(FLAGS.SUBTITLE_DIRECTORY_FLAG):
            name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, file_flag=file_flag))
            season = offrmod.retrieve_season(path=aux, verbose=verbose)
            episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
            subtitle = offrmod.retrieve_subtitles_directory(path=aux, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SUBTITLE_FLAG):
            name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, file_flag=file_flag))
            season = offrmod.retrieve_season(path=aux, verbose=verbose)
            episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
            language = onrmod.retrieve_str_language(path=path, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SEASON_DIRECTORY_FLAG):
            name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, file_flag=file_flag))
            season = offrmod.retrieve_season_directory(path=aux, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SHOW_DIRECTORY_FLAG):
            name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, file_flag=file_flag))
            season = offrmod.retrieve_season(path=aux, verbose=verbose)
            episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
            ename = onrmod.retrieve_episode_name(show_name=name, season=season, episode=episode, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SHOW_FLAG):
            name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, file_flag=file_flag))
            season = offrmod.retrieve_season(path=aux, verbose=verbose)
            episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
            ename = onrmod.retrieve_episode_name(show_name=name, season=season, episode=episode, verbose=verbose)

        elif int(file_flag) == int(FLAGS.FILM_DIRECTORY_FLAG):
            name = prettify_title(offrmod.retrieve_film_name(path=aux, verbose=verbose))
            year = offrmod.retrieve_film_year(path=aux, verbose=verbose)
            film_flag = str(offrmod.retrieve_film_flags(path=aux, verbose=verbose)).replace('.', ' ')

        elif int(file_flag) == int(FLAGS.FILM_FLAG):
            name = prettify_title(offrmod.retrieve_film_name(path=aux, verbose=verbose))
            year = offrmod.retrieve_film_year(path=aux, verbose=verbose)
            film_flag = str(offrmod.retrieve_film_flags(path=aux, verbose=verbose)).replace('.', ' ')

        elif int(file_flag) == int(FLAGS.ANIME_FLAG):
            name = prettify_title(offrmod.retrieve_anime_name(path=aux, verbose=verbose))
            episode = offrmod.retrieve_anime_episode(path=aux, verbose=verbose)

        elif int(file_flag) == int(FLAGS.ANIME_DIRECTORY_FLAG):
            name = prettify_title(offrmod.retrieve_anime_name(path=aux, verbose=verbose))
            episode = offrmod.retrieve_anime_episode(path=aux, verbose=verbose)

        elif int(file_flag) == int(FLAGS.UNKOWN_FLAG):
            name = aux

        quality = offrmod.retrieve_quality(path=aux, verbose=verbose)
        extension = offrmod.retrieve_extension(path=aux, verbose=verbose)

        if deep:
            codec = offrmod.retrieve_codec(path=aux, verbose=verbose)
            audio = offrmod.retrieve_audio(path=aux, verbose=verbose)
            uploader = offrmod.retrieve_uploader(path=aux, verbose=verbose)
            source = offrmod.retrieve_source(path=aux, verbose=verbose)

            metadata.set_codec(codec=codec)
            metadata.set_audio(audio=audio)
            metadata.set_uploader(uploader=uploader)
            metadata.set_source(source=source)

        metadata.set_name(name=name)
        metadata.set_season(season=season)
        metadata.set_episode(episode=episode)
        metadata.set_ename(ename=ename)
        metadata.set_quality(quality=quality)
        metadata.set_extension(extension=extension)
        metadata.set_language(language=language)
        metadata.set_year(year=year)
        metadata.set_film_flag(film_flag=film_flag)
        metadata.set_subtitle(subtitle)
        metadata.set_file_flag(file_flag=file_flag)

        message = 'standard metada'
        log_debug(message)
        message = str(name), str(ename), str(episode), str(season), str(quality), str(extension), str(language)
        log_debug(message)
        message = ' extended metada'
        log_debug(message)
        message = str(audio), str(codec), str(uploader), str(source), str(file_flag), str(film_flag), str(subtitle)
        log_debug(message)

    except Exception as e:
        print (e)
        return
    else:
        return metadata


def retrieve_usefull_path(path):
    usefull_path = os.path.basename(os.path.normpath(path))
    return usefull_path


def build_library_name(name):
    return str(name)


def build_show_directory_name(name, season, episode, ename, quality):
    if ename in '':
        directory_show_name = str(name) + ' S' + str(season) + 'E' + str(episode) + '[' + str(quality) + ']'
    else:
        directory_show_name = str(name) + ' S' + str(season) + 'E' + str(episode) + ' - ' + \
                   str(ename) + ' - ' + '[' + str(quality) + ']'
    return directory_show_name


def build_show_name(name, season, episode, ename, quality, extension):
    if ename in '':
        show_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) + '[' + str(quality) + ']' +\
                   str(extension)
    else:
        show_name = str(name) + ' S' + str(season) + 'E'  + str(episode) + ' - ' +\
                   str(ename) + ' - ' + '[' + str(quality) + ']' + str(extension)
    return show_name


def build_subtitle_directory_name(name, season, episode, subtitle):
    show_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) + '(' + str(subtitle) + ')'
    return show_name


def build_subtitle_name(name=str, season=str, episode=str, language=str, extension=str):
    if language in '':
        subtitle_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) +  str(extension)
    else:
        subtitle_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) + '(' + str(language) + ')' + str(extension)
    return subtitle_name


def build_season_directory_name(name=str, season=str):
    season_directory_name = str(name) + ' [Season ' + str(season) + ']'
    return season_directory_name


def build_film_directory_name(name=str, year=str, film_flag=str):
    if film_flag in '':
        film_directory_name = str(name) + ' (' + str(year) + ')'
    else:
        film_directory_name = str(name) + ' (' + str(year) + ') ' + str(film_flag)
    return film_directory_name


def build_film_name (name=str, year=str, film_flag=str, extension=str):
    if film_flag in '':
        film_name = str(name) + ' (' + str(year) + ')' + str(extension)
    else:
        film_name = str(name) + ' (' + str(year) + ') ' + str(film_flag) + str(extension)
    return film_name


def build_anime_name(name=str, episode=str, quality=str, extension=str):
    if quality in '':
        anime_name = str(name) + ' E' + str(episode) + str(extension)
    else:
        anime_name = str(name) + ' E' + str(episode) + '[' + str(quality) + ']' + str(extension)
    return anime_name


def build_anime_directory_name(name=str, episode=str, quality=str):
    if quality in '':
        anime_directory_name = str(name) + ' E' + str(episode)
    else:
        anime_directory_name = str(name) + ' E' + str(episode) + '[' + str(quality) + ']'
    return anime_directory_name


def rebuild_name(meta, verbose=None):

    new_name = ''
    name = meta.get_name()
    season = meta.get_season()
    episode = meta.get_episode()
    quality = meta.get_quality()
    subtitle = meta.get_subtitle()
    ename = meta.get_ename()
    extension = meta.get_extension()
    language = meta.get_language()
    film_flag = meta.get_film_flag()
    year = meta.get_year()
    file_flag = meta.get_file_flag()

    try:
        if int(file_flag) == int(FLAGS.LIBRARY_DIRECTORY_FLAG):
            new_name = build_library_name(name=name)

        elif int(file_flag) == int(FLAGS.SHOW_DIRECTORY_FLAG):
            new_name = build_show_directory_name(name=name, season=season, episode=episode, ename=ename, quality=quality)

        elif int(file_flag) == int(FLAGS.SHOW_FLAG):
            new_name = build_show_name(name=name, season=season, episode=episode, ename=ename, quality=quality, extension=extension)

        # todo Refinar
        elif int(file_flag) == int(FLAGS.TRASH_FLAG):
            new_name = 'rm -f *.nfo/.txt!!'

        elif int(file_flag) == int(FLAGS.SUBTITLE_FLAG):
            new_name = build_subtitle_name(name=name, season=season, episode=episode,language=language, extension=extension)

        # todo Refinar
        elif int(file_flag) == int(FLAGS.SUBTITLE_DIRECTORY_FLAG):
            new_name = build_subtitle_directory_name(name=name, season=season, episode=episode, subtitle=subtitle)

        elif int(file_flag) == int(FLAGS.SEASON_DIRECTORY_FLAG):
            new_name = build_season_directory_name(name=name, season=season)

        elif int(file_flag) == int(FLAGS.FILM_DIRECTORY_FLAG):
            new_name = build_film_directory_name(name=name, year=year, film_flag=film_flag)

        elif int(file_flag) == int(FLAGS.FILM_FLAG):
            new_name = build_film_name(name=name, year=year, film_flag=film_flag, extension=extension)

        elif int(file_flag) == int(FLAGS.ANIME_FLAG):
            new_name = build_anime_name(name=name, episode=episode, quality=quality, extension=extension)

        elif int(file_flag) == int(FLAGS.ANIME_DIRECTORY_FLAG):
            new_name = build_anime_directory_name(name=name, episode=episode, quality=quality)

    except Exception as e:
        print (e)
        return
    else:
        message = '(Rebuilded Name: \n' + '[Item]: < ' + new_name + ' >)'
        log_debug(message)
        return new_name
