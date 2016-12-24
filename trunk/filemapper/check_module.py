#!/usr/bin/python

import re
import os

def check_unwanted_files(path=None):
    statinfo = os.stat(path)
    print (str(int(statinfo.st_size)*1024*1024))


def check_multimedia (path=None):
    try:
        re.search('(\.mkv)|(\.mp4)$',path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_season_directory (path=None):
    try:
        re.search('(((\(|\[)?)season)(\-|\s|\.)?(\d{1,2})((\)|\])?)',path,re.IGNORECASE).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_subtitles_directory (path=None):
    try:
        re.search('((sub)|(subs)|(subtitle)|(subtitles))', path).group(0)
    except Exception as e:
        return False
    else:
        return True


def check_subtitles (path=None):
    try:
        re.search('(\.sub)|(\.str)', path).group(0)
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
