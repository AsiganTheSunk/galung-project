from enum import Enum

class FileFlags(Enum):
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
