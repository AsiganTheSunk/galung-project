#!/usr/bin/python

import re
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


def validate_directory_tree (path=None, verbose=None, file_flag=None):
    try:
        if(file_flag in FLAGS.SHOW_DIRECTORY_FLAG):
            valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))', path)
        elif(file_flag in FLAGS.SHOW_FLAG or FLAGS.TRASH_FLAG or FLAGS.TRASH_FLAG):
            valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))(\.mkv|\.mp4)', path)
        elif(file_flag in FLAGS.SEASON_DIRECTORY_FLAG):
            valid = re.search('(\w+\s)*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))(\.mkv|\.mp4)', path)
    except Exception as e:
        valid = 'None'
    else:
        if (verbose):
            print ('[INFO]: Current item: ' + valid +' -- [VALID]')
        return

