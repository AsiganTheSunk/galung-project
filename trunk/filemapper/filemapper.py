#!/usr/bin/python

import os
# import tvdb_api
from enum import Enum

import trunk.filemapper.check_module as cmod
import trunk.filemapper.retrieve_module as rmod
from trunk.datastructure.TreeRoot import TreeRoot
from trunk.datastructure.Metadata import Metadata


# FLAGS: to be moved to somewhere else.
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

directory_dict = {}
tOriginal = TreeRoot()
tUpdated = TreeRoot()

def directory_mapper(path=None):
    for root, directories, files in os.walk(path):
        for directory in directories:
            try:
                if cmod.check_season_directory(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.SEASON_DIRECTORY_FLAG
                elif cmod.check_subtitles_directory(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.SUBTITLE_DIRECTORY_FLAG
                elif cmod.check_film_type(directory):
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.FILM_DIRECTORY_FLAG
                else:
                    directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = FLAGS.SHOW_DIRECTORY_FLAG
            except Exception as e:
                continue

        for file in files:
            try:
                if cmod.check_unwanted(file):
                    directory_dict[str(os.path.abspath(os.path.join(root, file)))] = FLAGS.TRASH_FLAG
                elif cmod.check_subtitles(file):
                    directory_dict[str(os.path.abspath(os.path.join(root, file)))] = FLAGS.SUBTITLE_FLAG
                elif cmod.check_season(file):
                    directory_dict[str(os.path.abspath(os.path.join(root, file)))] = FLAGS.SHOW_FLAG
                elif cmod.check_film_type(file):
                    directory_dict[str(os.path.abspath(os.path.join(root, file)))] = FLAGS.FILM_FLAG
            except Exception as e:
                continue
    return (directory_dict)

# Estoy devolviendo tUpdated()
def build_directory_tree(basedir=None, directory=None, verbose=True):
    try:
        tOriginal.add_node(basename=str(os.path.basename(basedir)))
        tUpdated.add_node(basename=str(os.path.basename(basedir)))
        for item in sorted(directory):
            len_aux = len(str(os.path.basename(item)))
            parent = item[:-len_aux - 1]
            new_basename = retrieve_show_info(path=str(os.path.basename(item)), verbose=verbose, file_flag=directory[item])
            if parent in basedir:
                new_parent_basename = retrieve_show_info(path=str(os.path.basename(parent)), verbose=verbose, file_flag=FLAGS.LIBRARY_DIRECTORY_FLAG)
            else:
                # todo no lanzar segunda busqueda si nodo hijo existe, recuperarlo por id, usando el node_count, asi aprovechas la forma del mapeo.
                new_parent_basename = retrieve_show_info(path=str(os.path.basename(parent)), verbose=verbose, file_flag=directory[parent])
            tOriginal.add_node(basename=str(os.path.basename(item)), parent_basename=str(os.path.basename(parent)))
            tUpdated.add_node(basename=new_basename, parent_basename=new_parent_basename)

            # if verbose:
                # print ('______' * 20)
                # print ('item_flag: ' + directory[item], 'Iitem: ' + str(os.path.basename(item)),
                #       'Iparent: ' + str(os.path.basename(parent)))
                # print ('item_flag: ' + directory[item], 'Oitem: ' + str(new_basename), 'Oparent: '
                #       + str(new_parent_basename))

        print ('______' * 20 + '\n')
        tOriginal.display()
        print ('______' * 20 + '\n')
        tUpdated.display()
        # for item in tUpdated.dictionary:
        #     try:
        #         tUpdated.create_show_index(item, retrieve_number_of_seasons(item))
        #     except:
        #         continue
        #rmod.map_show_seasons(tUpdated)
        #tUpdated.create_season_index()
    except Exception as e:
        print (str('build-directory-tree: ') +str(e))
    else:
        return tUpdated


def list_directory():
    for item in sorted(directory_dict):
        print ('item_flag: '+ directory_dict[item], 'path: '+ item)


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
    except:
        return path
    else:
        return new_path


# todo con eso el mapeo esta finalizado, solo falta usar el objeto de Metadatos para almacenar la info
def retrieve_show_info (path=None, verbose=None, file_flag=None, deep=None, debug=None):
    meta = Metadata()
    film_flag=year=''
    show=season=episode=ename = ''
    subtitle=audio=codec=uploader=source = ''

    try:
        if int(file_flag) == int(FLAGS.LIBRARY_DIRECTORY_FLAG):
            return path

        elif int(file_flag) == int(FLAGS.SUBTITLE_DIRECTORY_FLAG):
            subtitle = rmod.retrieve_subtitles_directory(path=path, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SUBTITLE_FLAG):
            return path
            # todo retrieve data to send to the tree node!!

        elif int(file_flag) == int(FLAGS.SEASON_DIRECTORY_FLAG):
            show = prettify_title(rmod.retrieve_show_name(path=path, verbose=verbose, file_flag=file_flag))
            season = rmod.retrieve_season_directory(path=path, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SHOW_DIRECTORY_FLAG):
            show = prettify_title(rmod.retrieve_show_name(path=path, verbose=verbose, file_flag=file_flag))
            season = rmod.retrieve_season(path=path, verbose=verbose)
            episode = rmod.retrieve_episode(path=path, verbose=verbose)
            ename = rmod.retrieve_episode_name(show_name=show, season=season, episode=episode, verbose=verbose)

        elif int(file_flag) == int(FLAGS.SHOW_FLAG):
            show = prettify_title(rmod.retrieve_show_name(path=path, verbose=verbose, file_flag=file_flag))
            season = rmod.retrieve_season(path=path, verbose=verbose)
            episode = rmod.retrieve_episode(path=path, verbose=verbose)
            ename = rmod.retrieve_episode_name(show_name=show, season=season, episode=episode, verbose=verbose)

        elif int(file_flag) == int(FLAGS.FILM_DIRECTORY_FLAG):
            show = prettify_title(rmod.retrieve_film_name(path=path, verbose=verbose))
            year = rmod.retrieve_film_year(path=path, verbose=verbose)
            film_flag = str(rmod.retrieve_film_flags(path=path, verbose=verbose)).replace('.', ' ')

        elif int(file_flag) == int(FLAGS.FILM_FLAG):
            show = prettify_title(rmod.retrieve_film_name(path=path, verbose=verbose))
            year = rmod.retrieve_film_year(path=path, verbose=verbose)
            film_flag = str(rmod.retrieve_film_flags(path=path, verbose=verbose)).replace('.', ' ')

        elif int(file_flag) == int(FLAGS.UNKOWN_FLAG):
            return path

        # todo Por ahora estoy devolviendo el nombre entero
        # elif int(file_flag) == int(FLAGS.SUBTITLE_FLAG):
            # show = rmod.retrieve_subtitle(path=path, verbose=verbose)

        quality = rmod.retrieve_quality(path=path, verbose=verbose)
        extension = rmod.retrieve_extension(path=path, verbose=verbose)
        language = rmod.retrieve_language(path=path, verbose=verbose)

        if deep:
            codec = rmod.retrieve_codec(path=path, verbose=verbose)
            audio = rmod.retrieve_audio(path=path, verbose=verbose)
            uploader = rmod.retrieve_uploader(path=path, verbose=verbose)
            source = rmod.retrieve_source(path=path, verbose=verbose)

        meta.set_name(name=show)
        meta.set_subtitle(subtitle)
        meta.set_season(season=season)
        meta.set_episode(episode=episode)
        meta.set_quality(quality=quality)
        meta.set_extension(extension=extension)
        meta.set_language(language=language)
        meta.set_codec(codec=codec)
        meta.set_audio(audio=audio)
        meta.set_uploader(uploader=uploader)
        meta.set_source(source=source)

        if debug:
            print ('([DEBUG]: standard metada )')
            print ('[DEBUG]: ' ,str(show), str(ename), str(episode), str(season), str(quality), str(extension), str(language))
            print ('([DEBUG]: extended metada )')
            print ('[DEBUG]: ', str(audio), str(codec), str(uploader), str(source))
            print ('______' * 20 + '\n')

    except Exception as e:
        print (e)
        return
    else:
        pretty_show = rebuild_name(show_name=show, season=season, episode=episode, quality=quality, subtitle=subtitle,
                                   ename=ename, extension=extension, language=language, film_flag=film_flag, year=year,
                                   verbose=verbose, file_flag=file_flag)
        return pretty_show


def retrieve_usefull_path (path=None, verbose=None):
    usefull_path = os.path.basename(os.path.normpath(path))
    return usefull_path


def rebuild_name (show_name=None, ename=None, season=None, episode=None, quality=None, extension=None,
                  uploader=None, source=None, year=None, film_flag=None, language=None, subtitle=None,
                  verbose=None, file_flag=None, debug=None):
    new_name=''

    try:
        if file_flag in FLAGS.SHOW_DIRECTORY_FLAG:
            if ename in '':
                new_name = str(show_name) + ' ' + str(season) + str(episode) + '[' + str(quality) + ']'
            else:
                new_name = str(show_name) + ' ' + str(season) + str(episode) + ' - ' + \
                           str(ename) + ' - ' + '[' + str(quality) + ']'

        elif file_flag in FLAGS.SHOW_FLAG:
            if ename in '':
                new_name = str(show_name) + ' ' + str(season) + str(episode) + '[' + str(quality) + ']' +\
                           str(extension)
            else:
                new_name = str(show_name) + ' ' + str(season) + str(episode) + ' - ' +\
                           str(ename) + ' - ' + '[' + str(quality) + ']' + str(extension)

        elif file_flag in FLAGS.TRASH_FLAG:
            new_name = 'rm -f *.nfo/.txt!!'

        elif file_flag in FLAGS.SUBTITLE_FLAG:
            if language in '':
                new_name = str(show_name) + str(extension)
            else:
                new_name = str(show_name) + ' (' + str(language) + ')' + str(extension)

        elif file_flag in FLAGS.SUBTITLE_DIRECTORY_FLAG:
            new_name = str(subtitle)

        elif file_flag in FLAGS.SEASON_DIRECTORY_FLAG:
            new_name = str(show_name) + ' ' + str(season)

        elif file_flag in FLAGS.FILM_DIRECTORY_FLAG:
            if film_flag in '':
                new_name = str(show_name) + ' (' + str(year) + ')'
            else:
                new_name = str(show_name) + ' (' + str(year) + ') ' + str(film_flag)
        elif file_flag in FLAGS.FILM_FLAG:
            if film_flag in '':
                new_name = str(show_name) + ' (' + str(year) + ')' + str(extension)
            else:
                new_name = str(show_name) + ' (' + str(year) + ') ' + str(film_flag) + str(extension)

    except Exception as e:
        print (e)
    else:
        if verbose:
            print ('[INFO]: REBUILDED NAME: \n' + '[INFO]: < ' + new_name + ' >')
            print ('______' * 20 + '\n')
        return new_name
