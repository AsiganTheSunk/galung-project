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


def create_dictionary():
    return {}

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

    for item in sorted(directory_dict):
        print 'item_flag: '+ directory_dict[item], 'path: '+ item


    return (directory_dict)

# todo no pilla bien los nombres de las series, o las esta categorizando mal.

def build_directory_tree(basedir=None, directory=None, verbose=True):
    try:
        tOriginal.add_node(basename=str(os.path.basename(basedir)))
        tUpdated.add_node(basename=str(os.path.basename(basedir)))
        #dictionary = []

        for item in sorted(directory):
            len_aux = len(str(os.path.basename(item)))
            parent = item[:-len_aux - 1]
            #todo que pelotas estoy haciendo aqui anadiendo a saco por nombre
            #print str(prettify_title(rmod.retrieve_show_name(path=os.path.basename(item), file_flag=directory[item])))
            #dictionary.append(prettify_title(rmod.retrieve_show_name(path=os.path.basename(item), file_flag=directory[item])))
            new_basename = retrieve_show_info(path=str(os.path.basename(item)), verbose=False, file_flag=directory[item])
            if parent in basedir:
                new_parent_basename = retrieve_show_info(path=str(os.path.basename(parent)), verbose=False, file_flag=FLAGS.LIBRARY_DIRECTORY_FLAG)
            else:
                #todo no lanzar segunda busqueda si nodo hijo existe, recuperarlo por id, usando el node_count, asi aprovechas la forma del mapeo.
                new_parent_basename = retrieve_show_info(path=str(os.path.basename(parent)), verbose=False, file_flag=directory[parent])
            tOriginal.add_node(basename=str(os.path.basename(item)), parent_basename=str(os.path.basename(parent)))
            tUpdated.add_node(basename=new_basename, parent_basename=new_parent_basename)

            if verbose:
                print ('______' * 20)
                print ('item_flag: ' + directory[item], 'Iitem: ' + str(os.path.basename(item)),
                       'Iparent: ' + str(os.path.basename(parent)))
                print ('item_flag: ' + directory[item], 'Oitem: ' + str(new_basename), 'Oparent: '
                       + str(new_parent_basename))

        #tUpdated.dictionary = set(dictionary)
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
        #tUpdated.find_show_seasons('Teen Wolf', rmod.retrieve_number_of_seasons('Teen Wolf'))
    except Exception as e:
        print (str('build-directory-tree: ') +str(e))

def gather_metadata():
    return

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


def retrieve_show_info (path=None, verbose=None, file_flag=None, deep=None):
    meta = Metadata()
    show = ''
    ename = ''
    season = ''
    episode = ''
    film_flag = ''
    year = ''
    try:
        print path, file_flag
        if int(file_flag) == int(FLAGS.LIBRARY_DIRECTORY_FLAG):
            return (path)
        elif int(file_flag) is int(FLAGS.SEASON_DIRECTORY_FLAG):
            season = rmod.retrieve_season_directory(path=path, verbose=verbose)
        elif int(file_flag) == (int(FLAGS.SHOW_DIRECTORY_FLAG) or int(FLAGS.SHOW_FLAG)):
            show = prettify_title(rmod.retrieve_show_name(path=path, verbose=verbose, file_flag=file_flag))
            season = rmod.retrieve_season(path=path, verbose=verbose)
            episode = rmod.retrieve_episode(path=path, verbose=verbose)
            ename = rmod.retrieve_episode_name(show_name=show, season=season, episode=episode, verbose=verbose)
        elif int(file_flag) == (int(FLAGS.FILM_DIRECTORY_FLAG) or int(FLAGS.FILM_FLAG)):
            show = prettify_title(rmod.retrieve_film_name(path=path, verbose=verbose))
            year = rmod.retrieve_film_year(path=path, verbose=verbose)
            film_flag = str(rmod.retrieve_film_flags(path=path, verbose=verbose)).replace('.', ' ')


        quality = rmod.retrieve_quality(path=path, verbose=verbose)
        extension = rmod.retrieve_extension(path=path, verbose=verbose)
        subtitle = rmod.retrieve_subtitles_directory(path=path, verbose=verbose)
        language = rmod.retrieve_language(path=path, verbose=verbose)
        # if (file_flag in FLAGS.SUBTITLE_DIRECTORY_FLAG):
        # unwanted = rmod.retrieve_unwanted(path=path, verbose=verbose)
        # if(deep_search):
        #    codec = rmod.retrieve_codec(path=path, verbose=verbose)
        #    audio = rmod.retrieve_audio(path=path, verbose=verbose)
        #    uploader = rmod.retrieve_uploader(path=path, verbose=verbose)
        #    source = rmod.retrieve_source(path=path, verbose=verbose)

        meta.set_name(show)
        meta.set_ename(ename)
        meta.set_season(season)
        meta.set_episode(episode)
        meta.set_subtitle(subtitle)
        meta.set_quality(quality)
        meta.set_extension(extension)
        meta.set_language(language)
        #meta.set_audio(audio)
        #meta.set_codec(codec)
        #meta.set_source(source)
        #meta.set_uploader(uploader)

        print ('[DEBUG]: ' + str(show), str(ename), str(episode), str(season), str(quality), str(extension))
        pretty_show = rebuild_name(show_name=show, season=season, episode=episode, quality=quality, subtitle=subtitle,
                                   ename=ename, extension=extension, language=language, film_flag=film_flag, year=year,
                                   verbose=verbose, file_flag=file_flag)
    except Exception as e:
        print (e)
        return
    else:
        return pretty_show



def retrieve_usefull_path (path=None, verbose=None):
    usefull_path = os.path.basename(os.path.normpath(path))
    return usefull_path


def rebuild_name (show_name=None, ename=None, season=None, episode=None, quality=None, extension=None,
                  uploader=None, source=None, year=None, film_flag=None, language=None, subtitle=None,
                  verbose=None, file_flag=None, debug=None):
    new_name=''
    # if debug:
    # print ('[DEBUG]: ' + str(show_name), str(ename), str(episode), str(season), str(quality), str(extension),
    #           str(uploader), str(source), str(year), str(film_flag), str(language), str(subtitle))
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
            new_name = 'To Be Removed!!'

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
        #return

    else:
        if verbose:
            print ('[INFO]: REBUILDED NAME: ' + new_name)
        return new_name
