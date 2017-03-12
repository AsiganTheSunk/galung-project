#!/usr/bin/python

import re
import os

def check_main_directory_show(path=None):
    check_anime = check_anime_dir(path=path)
    check_season = check_season_directory(path=path)
    check_film = check_film_type(path=path)
    check_show = check_show_directory(path=path)
    check_sub = check_subtitles_directory(path=path)

    # print 'check_main_directory: ', check_anime, check_season, check_film, check_show
    if check_anime or check_season or check_show or check_film or check_sub:
        return False
    return True


def check_show_subtitles(path=None):
    check_serie = check_show(path=path)
    check_sub = check_subtitles(path=path)
    # print('show subtitles: ' + str(path))
    # print('show subs check: ', check_serie, check_sub)
    if check_serie and check_sub:
        return True

    return False


def check_show_subtitles_directory(path=None):
    check_show_dir = check_show(path=path)
    check_sub = check_subtitles_directory(path=path)
    #print('show subtitles: ' + str(path))
    #print('show showdir, sub, season: ', check_show_dir, check_sub, check_season )
    if check_show_dir and check_sub:
        return True
    return False


def check_anime_subtitles(path=None):
    check_anime = check_anime_show2(path=path)
    check_sub = check_subtitles(path=path)
    # print('anime subtitles:' + str(path))
    # print('anime subs check: ', check_anime, check_sub)
    if check_anime and check_sub:
        return True
    return False


def check_anime_subtitles_directory(path=None):
    check_anime = check_anime_dir(path=path)
    check_sub = check_subtitles_directory(path=path)
    # print('anime subtitles directory' + str(path))
    # print('anime subs check directory: ', check_anime, check_sub)
    if check_anime and check_sub:
        return True
    return False


def check_film_subtitles_directory(path=None):
    check_film_dir = check_film_type(path=path)
    check_sub = check_subtitles_directory(path=path)
    # print('film subtitles directory' + str(path))
    # print('film subs check directory: ', check_film_dir, check_sub)
    if check_film_dir and check_sub:
        return True
    return False


def check_film_subtitles(path=None):
    check_film = check_film_type(path=path)
    check_sub = check_subtitles(path=path)
    # print('film subtitles' + str(path))
    # print('film subs check: ', check_film, check_sub)
    if check_film and check_sub:
        return True
    return False


def check_unwanted(path=None):
    try:
        re.search('(\.com|\.txt|\.nfo)', path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_multimedia (path=None):
    try:
        re.search('(\.mkv|\.mp4)',path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_season_directory (path=None):
    try:
        re.search('(\-|\s|\.)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?', path, re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True


# todo hace falta rehacer esta funcion!! para los ejemplos de los subtitulos
def check_subtitles_directory (path=None):
    try:
        re.search('((subtitle)|(subtitles))', path, re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_subtitles(path=None):
    try:
        re.search('(\.sub|\.srt|\.ass)', path).group(0)
    except Exception as e:
        return False
    else:
        return True


# TODO Reisar esta funcion y sus efectos en el mapper deberia ser mas estricta solo permitiendo s01e01 y para el caso de temporadas
# TODO que fuese solo S01
def check_show(path=None):
    try:
        re.search('([s]\d{1,2}[e]\d{1,2})',path,re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True


# TODO n oes demasiado estricto en cuanto a ser un discriminante del tipo pelicula
def check_film_type (path=None):
    try:
        re.search('(.*)(([1-2])([890])(\d{2}))(?!p)', path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_anime_dir(path=None):
    try:
        #re.search('\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, re.IGNORECASE).group(0)
        #re.search('\[(\w+!?)\]|\[(\w+\-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, re.IGNORECASE).group(0)
        re.search('^\[(\w+(\s|\-|.?))+\]', path, re.IGNORECASE).group(0)
        re.search('\-(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}', path, re.IGNORECASE).group(0)
    except:
        return False
    else:
        return True


# TODO: Ver que hacer con esta funcion, que hace practicamente lo mismo que la normal
def check_anime_show2(path=None):
    try:
        re.search('^\[(\w+(\s|\-|.?))+\]', path, re.IGNORECASE).group(0)
        re.search('(\-)(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}', path, re.IGNORECASE).group(0)
    except:
        return False
    else:
        return True


def check_anime_show(path=None):
    try:
        re.search('\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?(.mp4|.mkv)', path, re.IGNORECASE).group(0)
    except Exception as e:
        try:
            re.search('^\[(\w+(\s|\-|.?))+\]', path, re.IGNORECASE).group(0)
            re.search('\-(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}', path, re.IGNORECASE).group(0)
            re.search('\.mp4|\.mkv', path, re.IGNORECASE).group(0)
        except:
            return False
        else:
            return True
    else:
        return True


def check_show_directory(path=None):
    try:
        re.search('(\w+.+)([s]\d{1,3}[e]\d{1,3}).?(\d{3,4}p).*(\[.*\])?', path, re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True
