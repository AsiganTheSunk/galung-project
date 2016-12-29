#!/usr/bin/python

import shutil
import os
from logging import DEBUG
from logging import basicConfig
from logging import debug as log_debug
from time import sleep
from trunk.filemapper.datastructure.Metadata import Metadata
from trunk.filemapper.datastructure.FileFlags import FileFlags as FLAGS
import trunk.filemapper.check.check_module as cmod
import trunk.filemapper.retrieve.offline_retrieve_module as offrmod
import trunk.filemapper.retrieve.online_retrieve_module as onrmod
from trunk.filemapper.datastructure.TreeRoot import TreeRoot


# TODO: FileMapper Validation

directory_dict = {}
tOriginal = TreeRoot()
tUpdated = TreeRoot()
basicConfig(filename=str(os.getcwd() + '/trunk/log/test.log'), filemode='w', format='%(filename)s %(message)s', level=DEBUG)

def directory_mapper(path=None, verbose=None):
    '''
    This function pre-maps the contents of the directory from a given path
    :param path:
    :param verbose:
    :return:
    '''
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
    '''
    This function creates a tree data structure from a given dictionary
    :param basedir: root node
    :param directory:
    :param verbose:
    :param debug:
    :param deep:
    :return:
    '''
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
    '''
    This function log the pre-map function into a file
    :param dict:
    :return:
    '''
    for item in sorted(dict):
        message = 'item_flag: ' + dict[item], 'path: ' + item
        log_debug(message)


def prettify_title(path=None):
    '''
    This function makes a name pretty
    :param path:
    :return:
    '''
    try:
        new_path = path.replace('-', ' ').replace('.', ' ').replace('_', ' ').rstrip().title()
    except Exception as e:
        return path
    else:
        return new_path


def retrieve_show_info(path=None, verbose=None, file_flag=None, deep=None, debug=None):
    '''
    This function retrieves info from a given path
    :param path:
    :param verbose:
    :param file_flag:
    :param deep:
    :param debug:
    :return:
    '''
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


def build_library_name(name):
    return str(name)


def build_show_directory_name(name, season, episode, ename, quality):
    '''
    This function builds a show name directory
    :param name:
    :param season:
    :param episode:
    :param ename:
    :param quality:
    :return:
    '''
    if ename in '':
        directory_show_name = str(name) + ' S' + str(season) + 'E' + str(episode) + '[' + str(quality) + ']'
    else:
        directory_show_name = str(name) + ' S' + str(season) + 'E' + str(episode) + ' - ' + \
                   str(ename) + ' - ' + '[' + str(quality) + ']'
    return directory_show_name


def build_show_name(name, season, episode, ename, quality, extension):
    '''
    This function builds a show name
    :param name:
    :param season:
    :param episode:
    :param ename:
    :param quality:
    :param extension:
    :return:
    '''
    if ename in '':
        show_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) + '[' + str(quality) + ']' +\
                   str(extension)
    else:
        show_name = str(name) + ' S' + str(season) + 'E'  + str(episode) + ' - ' +\
                   str(ename) + ' - ' + '[' + str(quality) + ']' + str(extension)
    return show_name


def build_subtitle_directory_name(name, season, episode, subtitle):
    '''
    This function builds a subtitle directory name
    :param name:
    :param season:
    :param episode:
    :param subtitle:
    :return:
    '''
    show_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) + '(' + str(subtitle) + ')'
    return show_name


def build_subtitle_name(name=str, season=str, episode=str, language=str, extension=str):
    '''
    This function builds a subtitle name
    :param name:
    :param season:
    :param episode:
    :param language:
    :param extension:
    :return:
    '''
    if language in '':
        subtitle_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) +  str(extension)
    else:
        subtitle_name = str(name) + ' S' + str(season) + 'E'  +  str(episode) + '(' + str(language) + ')' + str(extension)
    return subtitle_name


def build_season_directory_name(name=str, season=str):
    '''
    This function builds a season name directory
    :param name:
    :param season:
    :return:
    '''
    season_directory_name = str(name) + ' [Season ' + str(season) + ']'
    return season_directory_name


def build_film_directory_name(name=str, year=str, film_flag=str):
    '''
    This function builds a film directory name
    :param name:
    :param year:
    :param film_flag:
    :return:
    '''
    if film_flag in '':
        film_directory_name = str(name) + ' (' + str(year) + ')'
    else:
        film_directory_name = str(name) + ' (' + str(year) + ') ' + str(film_flag)
    return film_directory_name


def build_film_name (name=str, year=str, film_flag=str, extension=str):
    '''
    This function builds a film name
    :param name:
    :param year:
    :param film_flag:
    :param extension:
    :return:
    '''
    if film_flag in '':
        film_name = str(name) + ' (' + str(year) + ')' + str(extension)
    else:
        film_name = str(name) + ' (' + str(year) + ') ' + str(film_flag) + str(extension)
    return film_name


def build_anime_name(name=str, episode=str, quality=str, extension=str):
    '''
    This function builds a anime name
    :param name:
    :param episode:
    :param quality:
    :param extension:
    :return:
    '''
    if quality in '':
        anime_name = str(name) + ' E' + str(episode) + str(extension)
    else:
        anime_name = str(name) + ' E' + str(episode) + '[' + str(quality) + ']' + str(extension)
    return anime_name


def build_anime_directory_name(name=str, episode=str, quality=str):
    '''
    This function builds a anime directory name
    :param name:
    :param episode:
    :param quality:
    :return:
    '''
    if quality in '':
        anime_directory_name = str(name) + ' E' + str(episode)
    else:
        anime_directory_name = str(name) + ' E' + str(episode) + '[' + str(quality) + ']'
    return anime_directory_name


def rebuild_name(meta, verbose=None):
    '''
    This function rebuilds the name of a show|movie|anime from a given metadata object
    :param meta:
    :param verbose:
    :return:
    '''
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


def library_goes_live(old_tree, new_tree, library):
    '''
    This function creates the new directory tree for the library
    :param old_tree:
    :param new_tree:
    :param library:
    :return:
    '''
    new_tree_list = new_tree.build_full_path_tree()
    old_tree_list = old_tree.build_full_path_tree()

    basedir = os.getcwd()
    list_index_files = []
    list_index_dir = []


    for index in range(1, len(old_tree_list), 1):
        current_item = basedir + old_tree_list[index]
        if os.path.isfile(current_item):
            list_index_files.append(index)

        if os.path.isdir(current_item):
            if os.listdir(current_item) != []:
                list_index_dir.append(index)

    # TODO: cambiar os.path.join(a,b) para compatibilidad con linux y windows
    for index in range(len(old_tree_list), len(new_tree_list), 1):
        new_file = basedir + '/result' + new_tree_list[index]
        if not os.path.exists(new_file):
            os.makedirs(new_file)

    for index in list_index_dir:
        new_file = basedir + '/result' +new_tree_list[index]
        if not os.path.exists(new_file):
            os.makedirs(new_file)

    for index in list_index_files:
        new_file = basedir + '/result' + new_tree_list[index]
        old_file = basedir + old_tree_list[index]
        try:
            os.rename(old_file, new_file)
        except Exception as e:
            print 'Error Moving File {current_file}, {error}'.format(current_file=old_file, error=str(e))

    try:
        library_basename = os.path.basename(library)
        shutil.rmtree(library, ignore_errors=True)
        os.rename(os.path.join(os.path.join(basedir, 'result'), library_basename), library)
        shutil.rmtree(os.path.join(basedir, 'result'), ignore_errors=True)
    except Exception as e:
        print e
