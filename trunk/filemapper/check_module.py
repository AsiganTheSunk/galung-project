#!/usr/bin/python


import re
import os

# todo hacer la criba por tam
def check_unwanted_files(path=None):
    statinfo = os.stat(path)
    print (str(int(statinfo.st_size)*1024*1024))


def check_multimedia (path=None):
    try:
        re.search('(\.mkv|\.mp4)$',path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_season_directory (path=None):
    try:
        # (?!p) <- que no contenga
        # retrieved = re.search('(((\(|\[)?)season)(\-|\s|\.)?(\d{1,2})((\)|\])?)',path,re.IGNORECASE).group(0)
        # retrieved = re.search('(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?(\-|\s|\.)(\d{3,4}p)?',path,re.IGNORECASE).group(0)
        retrieved = re.search('(\-|\s|\.)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?', path, re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True

# todo hace falta rehacer esta funcion!! para los ejemplos de los subtitulos
def check_subtitles_directory (path=None):
    try:
        re.search('((sub)|(subs)|(subtitle)|(subtitles))', path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_subtitles (path=None):
    try:
        re.search('(\.sub|\.srt)', path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_season (path=None):
    try:
        re.search('([s]\d{1,2})',path,re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_unwanted (path=None):
    try:
        re.search('(\.nfo)|(\.txt)', path).group(0)
    except Exception as e:
        return False
    else:
        return True


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
        re.search('\[(\w+!?)\]|\[(\w+\-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, re.IGNORECASE).group(0)
    except:
        return False
    else:
        return True


def check_anime_show(path=None):
    try:
        re.search('\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?(.mp4|.mkv)', path, re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True

def check_show_directory(path=None):
    try:
        re.search('(\w+.+)([s]\d{1,3}[e]\d{1,3}).?(\d{3,4}p).*(\[.*\])?', path, re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True
