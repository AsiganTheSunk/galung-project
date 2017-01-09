#!/usr/bin/python
from trunk.filemapper.datastructure.FileFlags import FileFlags as FFLAGS
import re

def validate_show_season_directory(path=None, verbose=None):
    try:
        season_directory = re.search('((\(|\[)?(season(.*)?(\d{1,2}))(\)|\])?)',path,re.IGNORECASE).group(0)
    except Exception as e:
        return False


def validate_show_name(path=None, verbose=None):
    try:
        valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))', path)
        if valid:
            return True
    except Exception as e:
        return False


def validate_directory_tree (path=None, verbose=None, fflag=None):
    try:
        if(fflag in FFLAGS.SHOW_DIRECTORY_FLAG):
            valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))', path)
        elif(fflag in FFLAGS.SHOW_FLAG or FFLAGS.IGNORE_FLAG or FFLAGS.IGNORE_FLAG):
            valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))(\.mkv|\.mp4)', path)
        elif(fflag in FFLAGS.SEASON_DIRECTORY_FLAG):
            valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))(\.mkv|\.mp4)', path)
    except Exception as e:
        valid = 'None'
    else:
        if (verbose):
            print ('[INFO]: Current item: ' + valid +' -- [VALID]')
        return

