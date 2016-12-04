#!/usr/bin/python
import os
import re
import tvdb_api
from enum import Enum


#FLAGS: to be moved to somewhere else.
class FLAGS (Enum):
    SHOW_DIRECTORY_FLAG = '1'           #Directory
    SEASON_DIRECTORY_FLAG = '2'         # Season show directory
    SHOW_FLAG = '3'                     # Multimedia file (.mkv, .mp4):
    SUBTITLE_DIRECTORY_FLAG = '4'       # Subtitle directory
    SUBTITLE_FLAG = '5'                 # Subtitle file (.str, .sub): files to be inyected with?
    FILM_DIRECTORY_FLAG = '6'           # Film directory
    FILM_FLAG = '7'                     # Multimedia file (.mk, .mp4):
    UNKOWN_FLAG = '8'                   # Unkown File Type:
    TRASH_FLAG = '9'                    # Unwanted File

uploader_list = ['FUM','DIMENSION','PODO','HorribleSubs','AnimeRG','ROVERS']
source_list = ['rartv','rarbg','ettv','RARBG']
basedir = os.getcwd()+'/temp'

# if path /sub /subs /subtitle or /subtitles
# move to ../ then call ffmpeg_str_injector (input_file=None, output_file=None_):
# esto llamara a subprocess y lanzara la funcion
directory_dict = {}

from TreeRoot import TreeRoot
from Node import Node

def directory_mapper(path=None, verbose=None):
    path = basedir
    #t = rTree_Root()
    for root, directories, files in os.walk(path):
        for directory in directories:
            try:
                #t.add_node(basename=str(os.path.basename(directory)), parent_basename=str(os.path.basename(root)))
                if(check_season_directory(directory)):
                    directory_dict[str(os.path.abspath(os.path.join(root,directory)))] = (FLAGS.SEASON_DIRECTORY_FLAG)
                elif(check_subtitles_directory(directory)):
                    directory_dict[str(os.path.abspath(os.path.join(root,directory)))] = (FLAGS.SUBTITLE_DIRECTORY_FLAG)
                elif(check_film_type(directory)):
                    directory_dict[str(os.path.abspath(os.path.join(root,directory)))] = (FLAGS.FILM_DIRECTORY_FLAG)
                else:
                    directory_dict[str(os.path.abspath(os.path.join(root,directory)))] = (FLAGS.SHOW_DIRECTORY_FLAG)
            except Exception as e:
                print 'PETADA'
                continue

        for file in files:
            try:
                #t.add_node(basename=str(os.path.basename(file)), parent_basename=str(os.path.basename(root)))
                if (check_unwanted(file)):
                    directory_dict[str(os.path.abspath(os.path.join(root,file)))] = (FLAGS.TRASH_FLAG)
                elif(check_subtitles(file)):
                    directory_dict[str(os.path.abspath(os.path.join(root,file)))] = (FLAGS.SUBTITLE_FLAG)
                elif(check_season(file)):
                    directory_dict[str(os.path.abspath(os.path.join(root,file)))] = (FLAGS.SHOW_FLAG)
                elif(check_film_type(file)):
                    directory_dict[str(os.path.abspath(os.path.join(root,file)))] = (FLAGS.FILM_FLAG)
            except Exception as e:
                continue

    list_mapped_directory (directory=directory_dict)
    #t.display()


def list_mapped_directory (directory=None):
    try:
        t2 = TreeRoot()
        t2.add_node(basename=str(os.path.basename(basedir)))
        for item in sorted(directory):
            aux = len(str(os.path.basename(item)))
            temp = item[:-aux-1]
            t2.add_node(basename=str(os.path.basename(item)),parent_basename=str(os.path.basename(temp)))
            print 'item_flag: '+directory[item], 'item: '+str(os.path.basename(item)), 'parent: '+ str(item[:-aux-1])
        #t2.display()
        #t2.subtree('Game.of.Thrones [Season 1]')
        #todo probar caso de ser vacio

    except Exception as e:
        print e


def check_unwanted_files(path=None):
    statinfo = os.stat(path)
    print str(int(statinfo.st_size)*1024*1024)



def run(verbose=None, debug=None):
    for item in sorted(directory_dict):
        usefull_path = retrieve_usefull_path (path=item,verbose=verbose)
        new_directory_name = prettify_show(path=usefull_path, verbose=verbose, debug=debug, file_flag=directory_dict[item])
        if(debug):
            print '[DEBUG]: CURRENT ITEM: '+usefull_path

        #new_path = os.path.join(item.replace(os.path.basename(item), ''), new_directory_name)
        #rename(path= item, new_path=new_path)
        #update_directory_dict(item, os.path.join(item.replace(os.path.basename(item), ''), new_directory_name))
        #elif(int(directory_dict[item]) == FLAGS.SHOW_FLAG):
        #    print 'SHOW_FLAG'


# No te vuelvas loco, falta por recorrer los sub directorios
def run2(verbose=None, debug=None):
    for item in sorted(directory_dict):
        usefull_path = retrieve_usefull_path (path=item,verbose=verbose)
        new_directory_name = prettify_film(path=usefull_path, verbose=verbose, debug=debug, file_flag=directory_dict[item])
        if(debug):
            print '[DEBUG]: CURRENT ITEM: '+usefull_path

        #new_path = os.path.join(item.replace(os.path.basename(item), ''), new_directory_name)
        #rename(path= item, new_path=new_path)
        #update_directory_dict(item, os.path.join(item.replace(os.path.basename(item), ''), new_directory_name))
        #rename(path= item, new_path=new_path)
        #update_directory_dict(item, os.path.join(item.replace(os.path.basename(item), ''), new_directory_name))


def update_directory_dict (old_path=None, new_path=None, verbose=None):
    try:
        file_flag = directory_dict[old_path]
        #print file_flag, old_path
        del directory_dict[old_path]
        directory_dict[new_path] = file_flag
        #print file_flag, new_path
        #list_directory(directory=directory_dict)
    except:
        return


def rename(path=None, new_path=None):
    try:
        os.rename(path, new_path)
    except Exception as e:
        return
    else:
        return


def prettify_string (path=None):
    try:
        new_path = path.replace('-',' ').replace('.',' ').replace('_',' ').rstrip().title()
    except:
        return path
    else:
        return new_path


def prettify_film(path=None, verbose=None, file_flag=None, debug=None, deep_search=None):
    pretty_film = ''
    try:
        if verbose:
            print '\n******************************************************'
            print '[INFO]: FILE_FLAG: ' + file_flag


        film_name = prettify_string(retrieve_film_name(path=path, verbose=verbose))
        film_year = retrieve_film_year(path=path, verbose=verbose)
        film_flag = str(retrieve_film_flags(path=path,verbose=verbose)).replace('.',' ')
        retrieve_language (path=path, verbose=verbose)
        extension = retrieve_extension(path=path, verbose=verbose)
        language = retrieve_language(path=path, verbose=verbose)
        #unwanted = retrieve_unwanted(path=path, verbose=verbose)

        #if (file_flag in FLAGS.SUBTITLE_DIRECTORY_FLAG):
        subtitle = retrieve_subtitles_directory(path=path, verbose=verbose)

        #if(deep_search):
        #    codec = retrieve_codec(path=path, verbose=verbose)
        #    audio = retrieve_audio(path=path, verbose=verbose)
        #    source = retrieve_source(path=path, verbose=verbose)

        if(debug):
            print '[DEBUG]: '+str(film_name), str(film_year), str(film_flag), str(extension), str(language), str(subtitle)

        pretty_film = rebuild_name(show_name=film_name, film_year=film_year, film_flag=film_flag, extension=extension, subtitle=subtitle,
                                   language = language, verbose=verbose, file_flag=file_flag, debug=debug)
    except Exception as e:
        print e
        return
    else:
        return pretty_film


def prettify_show(path=None, verbose=None, file_flag=None, debug=None, deep_search=None):
    pretty_show=''
    try:
        if verbose:
            print '\n******************************************************'
            print '[INFO]: FILE_FLAG: ' + file_flag

        show = prettify_string(retrieve_show_name(path=path, verbose=verbose,file_flag=file_flag))
        episode = retrieve_episode(path=path, verbose=verbose)

        if (file_flag in FLAGS.SEASON_DIRECTORY_FLAG):
            season = retrieve_season_directory(path=path, verbose=verbose)
        else:
            season = retrieve_season(path=path, verbose=verbose)

        #if (file_flag in FLAGS.SUBTITLE_DIRECTORY_FLAG):
        subtitle = retrieve_subtitles_directory(path=path, verbose=verbose)

        quality = retrieve_quality(path=path, verbose=verbose)
        episode_name = retrieve_episode_name (show_name=show,season=season,episode=episode,verbose=verbose)
        extension = retrieve_extension(path=path, verbose=verbose)
        language = retrieve_language (path=path, verbose=verbose)
        #unwanted = retrieve_unwanted(path=path, verbose=verbose)

        #if(deep_search):
        #    codec = retrieve_codec(path=path, verbose=verbose)
        #    audio = retrieve_audio(path=path, verbose=verbose)
        #    uploader = retrieve_uploader(path=path, verbose=verbose)
        #    source = retrieve_source(path=path, verbose=verbose)
        if(debug):
            print '[DEBUG]: '+str(show), str(episode_name), str(episode), str(season), str(quality), str(extension)
        pretty_show = rebuild_name (show_name=show, season=season, episode=episode, quality=quality, subtitle=subtitle,
                                    episode_name=episode_name, extension=extension, language=language,
                                    verbose=verbose, file_flag=file_flag, debug=debug)
    except Exception as e:
        print e
        return
    else:
        return pretty_show


#os.rename(os.path.join(basedir,item),fullpath)
def retrieve_usefull_path (path=None, verbose=None):
    usefull_path = os.path.basename(os.path.normpath(path))
    return usefull_path


def rebuild_name (show_name=None, episode_name=None, season=None, episode=None, quality=None, extension=None,
                  uploader=None, source=None, film_year=None, film_flag=None, language=None, subtitle=None,
                  verbose=None, file_flag=None, debug=None):
    #new_name=''
    if(debug):
        print '[DEBUG]: '+str(show_name), str(episode_name), str(episode), str(season), str(quality), str(extension), \
            str(uploader), str(source), str(film_year), str(film_flag), str(language), str(subtitle)
    try:
        if(file_flag in FLAGS.SHOW_DIRECTORY_FLAG):
            if (episode_name in ''):
                new_name = str(show_name)+' '+ str(season) + str(episode)+'['+str(quality)+']'
            else:
                new_name = str(show_name)+' '+ str(season) + str(episode)+' - '+str(episode_name)+' - '+'['+str(quality)+']'

        elif(file_flag in FLAGS.SHOW_FLAG):
            if (episode_name in ''):
                new_name = str(show_name)+' '+ str(season) + str(episode)+'['+str(quality)+']'+str(extension)
            else:
                new_name = str(show_name)+' '+ str(season) + str(episode)+' - '+str(episode_name)+' - '+'['+str(quality)+']'+str(extension)

        elif(file_flag in FLAGS.TRASH_FLAG):
                new_name =  'To Be Removed!!'

        elif(file_flag in FLAGS.SUBTITLE_FLAG):
            if (language in ''):
                new_name = str(show_name)+str(extension)
            else:
                new_name = str(show_name)+' ('+str(language)+') '+str(extension)

        elif(file_flag in FLAGS.SUBTITLE_DIRECTORY_FLAG):
                new_name = str(subtitle)

        elif(file_flag in FLAGS.SEASON_DIRECTORY_FLAG):
                new_name = str(show_name)+' '+'['+str(season)+']'

        elif(file_flag in FLAGS.FILM_DIRECTORY_FLAG):
            if (film_flag in ''):
                new_name = str(show_name)+' ('+str(film_year)+')'
            else:
                new_name = str(show_name)+' ('+str(film_year)+') '+str(film_flag)
        elif(file_flag in FLAGS.FILM_FLAG):
            if (film_flag in ''):
                new_name = str(show_name)+' ('+str(film_year)+')'+str(extension)
            else:
                new_name = str(show_name)+' ('+str(film_year)+') '+str(film_flag)+str(extension)

    except Exception as e:
        print e
    else:
        if (verbose):
            print '[INFO]: REBUILDED NAME: '+new_name
        return new_name


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

#BRRip, HDRip, BluRay
def retrieve_quality (path=None, verbose=None):
    quality=''
    try:
        quality = re.search ('((\d{3,4}p))',path).group(0)
    except Exception as e:
        quality=''
        return quality
    else:
        if(verbose):
            print '[INFO]: QUALITY:'+ quality
        return quality


def retrieve_episode (path=None, verbose=None):
    try:
        episode = re.search ('([e])\d{2,3}', path,re.IGNORECASE).group(0)
    except Exception as e:
        episode = ''
        return episode
    else:
        if(verbose):
            print '[INFO]: EPISODE: '+episode
        return episode


def retrieve_season_directory (path=None, verbose=None):
    try:
        #re.search ('([s]\d{1,2})([e]\d{2,3})?!', path, re.IGNORECASE)
        season_directory = re.search('(((\(|\[)?)season)(\-|\s|\.)?(\d{1,2})((\)|\])?)', path, re.IGNORECASE).group(0)
    except Exception as e:
        season_directory =''
        return season_directory
    else:
        if(verbose):
            print '[INFO]: SEASON_DIRECTORY: '+season_directory
        return season_directory


def retrieve_season (path=None, verbose=None):
    try:
        season = re.search('([s]\d{2})',path,re.IGNORECASE).group(0)
        #season = re.search ('([S-s][E-e][A-a][S-s][O-o][N-n](.*)(\d))', path).group(0)
    except Exception as e:
        season = ''
        return season
    else:
        if(verbose):
            print '[INFO]: SEASON: '+season
        return season


def retrieve_audio (path=None, verbose=None):
    try:
        audio = re.search('((ACC)|(AC3)|(DTS)|(DD5\.1)|(ACC2\.0)|(MP3))', path,re.IGNORECASE).group(0)
    except Exception as e:
        audio = ''
        return audio
    else:
        if(verbose):
            print '[INFO]: AUDIO: '+audio
        return audio


def retrieve_codec (path=None, verbose=None):
    try:
        codec = re.search('((x264)|(H264)|(x265)|(H265)|(XviD))', path).group(0)
    except Exception as e:
        codec = ''
        return codec
    else:
        if(verbose):
            print '[INFO]: CODEC: '+codec
        return codec


def retrieve_extension (path=None, verbose=None):
    try:
        #if (os.path.isfile(path)):
        extension = re.search('(((\.mkv)|(\.mp4))$)', path).group(0)
    except Exception as e:
        extension = ''
        return extension
    else:
        if (verbose):
            print '[INFO]: EXTENSION: '+extension
        return extension


def retrieve_source (path=None, verbose=None):
    for item in source_list:
        try:
            source = re.search ('((\[)?'+re.escape(item)+'(\])?)',path).group(0)
        except Exception as e:
            source = ''
            return source
        else:
            if(verbose):
                print ('[INFO]: SOURCE: '+source)
            return source


def retrieve_uploader (path=None, verbose=None):
    for item in uploader_list:
        try:
            uploader = re.search ('((\[)?'+re.escape(item)+'(\])?)',path).group(0)
        except Exception as e:
            uploader = ''
            return uploader
        else:
            if(verbose):
                print ('[INFO]: UPLOADER: '+uploader)
            return uploader


def retrieve_language (path=None, verbose=None):
    try:
        language = re.search('(\()(en(glish)?)(\))|(\()(es|(spanish))(\))', path, re.IGNORECASE).group(0)
    except Exception as e:
        language = ''
        return language
    else:
        if(verbose):
            print '[INFO]: LANGUAGE: '+language
        return language[1:-1]


def retrieve_unwanted (path=None, verbose=None):
    try:
        unwanted = re.search('(((\.txt)|(\.nfo))$)', path).group(0)
    except Exception as e:
        unwanted = ''
        return unwanted
    else:
        unwanted = path
        if (verbose):
            print '[INFO]: SUBTITLE: '+unwanted
        return unwanted


def retrieve_subtitles_directory (path=None, verbose=None):
    try:
        subtitle_directory = re.search('((sub)|(subs)|(subtitle)|(subtitles))', path, re.IGNORECASE).group(0)
    except Exception as e:
        subtitle_directory=''
        return subtitle_directory
    else:
        if (verbose):
            print '[INFO]: SUBTITLE: '+subtitle_directory
        return subtitle_directory


def retrieve_subtitles (path=None, verbose=None):
    try:
        subtitles = re.search('(((\.str)|(\.sub))$)', path).group(0)
    except Exception as e:
        subtitles = ''
        return subtitles
    else:
        if (verbose):
            print '[INFO]: SUBTITLE: '+path
        return path


def retrieve_film_flags (path=None, verbose=None):
    try:
        film_flag = re.search('(EXTENDED(.*)?CUT|REMASTERED)',path, re.IGNORECASE).group(0)
    except Exception as e:
        film_flag = ''
        return film_flag
    else:
        if(verbose):
            print '[INFO]: FILM_FLAG: '+film_flag
        return film_flag


def retrieve_film_name (path=None, verbose=None):
    try:
        aux_lenth = re.search('(([1-2])([890])(\d{2}))(?!p)', path).group(0)
        film_name = re.search('(.*)(([1-2])([890])(\d{2}))(?!p)', path).group(0)[:-(len(aux_lenth))]
    except Exception as e:
        film_name = ''
        return film_name
    else:
        if(verbose):
            print '[INFO]: FILM_NAME: '+film_name
        return film_name


def retrieve_film_year (path=None, verbose=None):
    try:
        film_year = re.search('(([1-2])([890])(\d{2}))(?!p)', path).group(0)
    except Exception as e:
        film_year = ''
        return film_year
    else:
        if(verbose):
            print '[INFO]: FILM_YEAR: '+film_year
        return film_year


def retrieve_show_name (path=None, verbose=None, file_flag=None):
    try:
        if(file_flag in FLAGS.SEASON_DIRECTORY_FLAG):
            aux_lenth = re.search('((\(|\[)?)season(\-|\s|\.)?(\d{1,2})((\)|\])?)', path, re.IGNORECASE).group(0)
            show_name = re.search('((.*)((\(|\[)?)season(\-|\s|\.)?(\d{1,2})((\)|\])?))', path, re.IGNORECASE).group(0)[:-len(aux_lenth)]
        else:
            aux_lenth = re.search('([s]\d{1,2})',path,re.IGNORECASE).group(0)
            show_name = re.search('(.*)([s]\d{1,2})', path,re.IGNORECASE).group(0)[:-len(aux_lenth)]
    except Exception as e:
        show_name = ''
        return show_name
    else:
        if(verbose):
            print '[INFO]: SHOW_NAME: '+ show_name
        return show_name


def retrieve_episode_name (show_name=None, season=None, episode=None, verbose=None):
    try:
        t = tvdb_api.Tvdb()
        episode = t[show_name][int(season[1:])][int(episode[1:])]
    except Exception as e:
        episode_name =''
        return episode_name
    else:
        if(verbose):
            print '[INFO]: EPISODE_NAME: '+episode['episodename']
        # hacer llamadas all tdbapi -> de morfa incremental en caso de que sea una preposicion, articulo etc, hacer un iter++
        # en caso de recibir multiples resultados
        return episode['episodename']


def validate_show_season_directory(path=None, verbose=None):
    try:
        season_directory = re.search('((\(|\[)?(season(.*)?(\d{1,2}))(\)|\])?)',path,re.IGNORECASE).group(0)
    except Exception as e:
        return False


def validate_show_name(path=None, verbose=None):
    try:
        valid = re.search('((\w+\s))*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))', path)
        if valid:
            return True
    except Exception as e:
        return False


def validate_directory_tree (path=None, verbose=None, file_flag=None):
    try:
        if(file_flag in FLAGS.SHOW_DIRECTORY_FLAG):
            valid = re.search('((\w+\s))*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))', path)
        elif(file_flag in FLAGS.SHOW_FLAG or FLAGS.TRASH_FLAG or FLAGS.TRASH_FLAG):
            valid = re.search('((\w+\s))*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))(\.mkv|\.mp4)', path)
        elif(file_flag in FLAGS.SEASON_DIRECTORY_FLAG):
            valid = re.search('((\w+\s))*([S]?\d{0,2})([E]\d{2,3})(\-\s(\w+\s)*(\-(\w+\s)*\[\d{3,4}[p]\]))(\.mkv|\.mp4)', path)
    except Exception as e:
        valid = 'None'
    else:
        if (verbose):
            print '[INFO]: Current item: ' + valid +' -- [VALID]'
        return


def remove_trash (path, verbose=None):
    try:
        file = re.search('(((\.txt)|(\.nfo))$)', path)
        #os.remove()
    except:
        file = 'None'
    else:
        if (verbose):
            print '[INFO]: Trash Found ('+path+') Removed'


def main():
    directory_mapper()
    #run(verbose=True, debug=True)


if __name__ == '__main__':
    main()
