from langdetect import DetectorFactory
from langdetect import detect
import tvdb_api
import pysrt
import chardet
import re

def retrieve_episode_name(show_name=str, season=str, episode=str, verbose=False):
    '''
    This function retrieves episode name values from a given show using tvdb_api
    :param show_name:
    :param season:
    :param episode:
    :param verbose:
    :return:
    '''
    try:
        t = tvdb_api.Tvdb()
        episode = t[show_name][int(season)][int(episode)]
    except Exception as e:
        episode_name = ''
        return episode_name
    else:
        if verbose:
            print ('[INFO]: EPISODE_NAME: ' + episode['episodename'])
        return episode['episodename']


def retrieve_number_of_episodes_per_season(name=None, season=None):
    '''
    This function retrieves number of episodes per season from a given show using tvdb_api
    :param name:
    :param season:
    :return:
    '''
    try:
        t = tvdb_api.Tvdb()
        episode_count =  len(t[name][int(season)])
    except tvdb_api.tvdb_error or tvdb_api.tvdb_episodenotfound:
        episode_count = 0
        return episode_count
    else:
        return episode_count


def retrieve_number_of_seasons(name=None):
    '''
    This function retrieves number of seasons from a given show using tvdb_api
    :param name:
    :return:
    '''
    try:
        t = tvdb_api.Tvdb()
        season_count = len(t[name])
    except tvdb_api.tvdb_error or tvdb_api.tvdb_seasonnotfound:
        season_count = 0
        return season_count
    else:
        return season_count

def retrieve_subtitles(path=None, verbose=None):
    try:
        subtitles = re.search('(\.str|\.sub)$', path).group(0)
    except Exception as e:
        subtitles = ''
        return subtitles
    else:
        if verbose:
            print ('[INFO]: SUBTITLE: ' + subtitles)
        return subtitles

def retrieve_str_language(path=None, verbose=False):
    '''
    This function retrieves language from a given path using re | langdetect
    :param path:
    :param verbose:
    :return:
    '''
    path = unicode(path, "utf-8")
    DetectorFactory.seed = 0
    lang = ''
    aux = ''
    try:
        lang = re.search('\((en|es|spanish|english)\)', path, re.IGNORECASE).group(0)
    except:
        try:
            with open(str(path), 'r') as myfile:
                data=myfile.read()
                encoding = chardet.detect(data)
                content = pysrt.open(path, encoding=encoding['encoding'])

                for i in range (0,15,1):
                    aux += ' ' + content[i].text

            lang = detect(aux)
        except:
            lang = ''
            return lang
        else:
            if verbose:
               print ('[INFO]: LANGUAGE: ' + str(lang))
            return lang
    else:
        if verbose:
               print ('[INFO]: LANGUAGE: ' + str(lang))
        return lang[1:-1]
