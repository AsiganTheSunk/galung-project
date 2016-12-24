#!/usr/bin/python

import re
import tvdb_api
from enum import Enum

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


uploader_list = ['FUM', 'DIMENSION', 'PODO', 'HorribleSubs', 'AnimeRG', 'ROVERS']
source_list = ['rartv', 'rarbg', 'ettv', 'RARBG']

# BRRip, HDRip, BluRay
def retrieve_quality(path=None, verbose=None):
    quality=''
    try:
        quality = re.search ('(\d{3,4}p)', path).group(0)
    except Exception as e:
        quality=''
        return quality
    else:
        if(verbose):
            print ('[INFO]: QUALITY:'+ quality)
        return quality


def retrieve_episode(path=None, verbose=None):
    try:
        episode = re.search ('([e])\d{2,3}', path, re.IGNORECASE).group(0)
    except Exception as e:
        episode = ''
        return episode
    else:
        if(verbose):
            print ('[INFO]: EPISODE: '+episode)
        return episode


def retrieve_season_directory(path=None, verbose=None):
    try:
        season_directory = re.search('(((\(|\[)?)season)(\-|\s|\.)?(\d{1,2})((\)|\])?)', path, re.IGNORECASE).group(0)
    except Exception as e:
        season_directory =''
        return season_directory
    else:
        if verbose:
            print ('[INFO]: SEASON_DIRECTORY: '+season_directory)
        return season_directory


def retrieve_season(path=None, verbose=None):
    try:
        season = re.search('([s]\d{2})',path, re.IGNORECASE).group(0)
    except Exception as e:
        season = ''
        return season
    else:
        if verbose:
            print ('[INFO]: SEASON: '+season)
        return season


def retrieve_audio(path=None, verbose=None):
    try:
        audio = re.search('((ACC)|(AC3)|(DTS)|(DD5\.1)|(ACC2\.0)|(MP3))', path, re.IGNORECASE).group(0)
    except Exception as e:
        audio = ''
        return audio
    else:
        if verbose:
            print ('[INFO]: AUDIO: '+audio)
        return audio


def retrieve_codec(path=None, verbose=None):
    try:
        codec = re.search('((x264)|(H264)|(x265)|(H265)|(XviD))', path).group(0)
    except Exception as e:
        codec = ''
        return codec
    else:
        if verbose:
            print ('[INFO]: CODEC: '+codec)
        return codec


def retrieve_extension(path=None, verbose=None):
    try:
        #if (os.path.isfile(path)):
        extension = re.search('(((\.mkv)|(\.mp4)|(\.str)|(\.sub))$)', path).group(0)
    except Exception as e:
        extension = ''
        return extension
    else:
        if verbose:
            print ('[INFO]: EXTENSION: '+extension)
        return extension


def retrieve_source(path=None, verbose=None):
    for item in source_list:
        try:
            source = re.search ('((\[)?' + re.escape(item) + '(\])?)', path).group(0)
        except Exception as e:
            source = ''
            return source
        else:
            if verbose:
                print ('[INFO]: SOURCE: '+source)
            return source


def retrieve_uploader(path=None, verbose=None):
    for item in uploader_list:
        try:
            uploader = re.search ('((\[)?'+re.escape(item)+'(\])?)',path).group(0)
        except Exception as e:
            uploader = ''
            return uploader
        else:
            if verbose:
                print ('[INFO]: UPLOADER: '+uploader)
            return uploader


def retrieve_language(path=None, verbose=None):
    try:
        language = re.search('(\()(en(glish)?)(\))|(\()(es|(spanish))(\))', path, re.IGNORECASE).group(0)
    except Exception as e:
        language = ''
        return language
    else:
        if verbose:
            print ('[INFO]: LANGUAGE: '+language)
        return language[1:-1]


def retrieve_unwanted(path=None, verbose=None):
    try:
        unwanted = re.search('(((\.txt)|(\.nfo))$)', path).group(0)
    except Exception as e:
        unwanted = ''
        return unwanted
    else:
        unwanted = path
        if verbose:
            print ('[INFO]: SUBTITLE: '+unwanted)
        return unwanted


def retrieve_subtitles_directory(path=None, verbose=None):
    try:
        subtitle_directory = re.search('sub\w{0,6}', path, re.IGNORECASE).group(0)
    except Exception as e:
        subtitle_directory = ''
        return subtitle_directory
    else:
        if verbose:
            print ('[INFO]: SUBTITLE: '+subtitle_directory)
        return subtitle_directory


def retrieve_subtitles(path=None, verbose=None):
    try:
        subtitles = re.search('(((\.str)|(\.sub))$)', path).group(0)
    except Exception as e:
        subtitles = ''
        return subtitles
    else:
        if verbose:
            print ('[INFO]: SUBTITLE: '+path)
        return path


def retrieve_film_flags(path=None, verbose=None):
    try:
        film_flag = re.search('(EXTENDED(.*)?CUT|REMASTERED)', path, re.IGNORECASE).group(0)
    except Exception as e:
        film_flag = ''
        return film_flag
    else:
        if verbose:
            print ('[INFO]: FILM_FLAG: '+film_flag)
        return film_flag


def retrieve_film_name(path=None, verbose=None):
    try:
        aux_lenth = re.search('(([1-2])([890])(\d{2}))(?!p)', path).group(0)
        film_name = re.search('(.*)(([1-2])([890])(\d{2}))(?!p)', path).group(0)[:-(len(aux_lenth))]
    except Exception as e:
        film_name = ''
        return film_name
    else:
        if verbose:
            print ('[INFO]: FILM_NAME: '+film_name)
        return film_name


def retrieve_film_year(path=None, verbose=None):
    try:
        film_year = re.search('(([1-2])([890])(\d{2}))(?!p)', path).group(0)
    except Exception as e:
        film_year = ''
        return film_year
    else:
        if verbose:
            print ('[INFO]: FILM_YEAR: '+film_year)
        return film_year


def retrieve_show_name(path=None, verbose=None, file_flag=None):
    try:
        if(file_flag in FLAGS.SEASON_DIRECTORY_FLAG):
            aux_lenth = re.search('((\(|\[)?)season(\-|\s|\.)?(\d{1,2})((\)|\])?)', path, re.IGNORECASE).group(0)
            show_name = re.search('((.*)((\(|\[)?)season(\-|\s|\.)?(\d{1,2})((\)|\])?))', path, re.IGNORECASE).group(0)[:-len(aux_lenth)]
        else:
            aux_lenth = re.search('([s]\d{1,2})', path, re.IGNORECASE).group(0)
            show_name = re.search('(.*)([s]\d{1,2})', path, re.IGNORECASE).group(0)[:-len(aux_lenth)]
    except Exception as e:
        show_name = ''
        return show_name
    else:
        if verbose:
            print ('[INFO]: SHOW_NAME: '+ show_name)
        return show_name


def retrieve_episode_name(show_name=None, season=None, episode=None, verbose=None):
    try:
        t = tvdb_api.Tvdb()
        episode = t[show_name][int(season[1:])][int(episode[1:])]
    except Exception as e:
        episode_name = ''
        return episode_name
    else:
        if verbose:
            print ('[INFO]: EPISODE_NAME: '+episode['episodename'])
        # hacer llamadas all tdbapi -> de morfa incremental en caso de que sea una preposicion, articulo etc, hacer un iter++
        # en caso de recibir multiples resultados
        return episode['episodename']

def map_show_seasons(obj):
    for item in obj.dictionary:
        try:
            obj.find_show_seasons(item, retrieve_number_of_seasons(item))
        except:
            continue


def retrieve_number_of_seasons(key=None):
    t = tvdb_api.Tvdb()
    season_count = 0
    try:
        for i in range(0, 30):
            if t[key][i]:
                season_count += 1
    except Exception as e:
        return season_count
