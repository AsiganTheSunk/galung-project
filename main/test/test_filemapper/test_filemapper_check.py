from main.filemapper.check import check_module as check

# Multimedia Check Tests
def test0_filemapper_check_multimedia():
    assert check.check_multimedia('multimedia_video_sample.mkv') is True


def test1_filemapper_check_multimedia():
    assert check.check_multimedia('multimedia_video_sample.mp4') is True


# TODO
def test1_filemapper_check_multimedia():
    assert check.check_multimedia('multimedia_video_sample.mp3') is False


# Multimedia Subtitle Directory Tests
def test0_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (subtitle)') is True


def test1_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (subtitles)') is True


# TODO
def test2_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (sub)') is False

# TODO
def test3_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (subs)') is False


#Multimedia Subtitle File Tests
def test0_filemapper_check_subtitle_file():
    assert check.check_subtitles('multimedia_subitle_sample.srt') is True


def test1_filemapper_check_subtitle_file():
    assert check.check_subtitles('multimedia_subitle_sample.ass') is True


def test2_filemapper_check_subtitle_file():
    assert check.check_subtitles('multimedia_subitle_sample.sub') is True


# Multimedia Show Directory/File Tests
def test0_filemapper_check_show():
    assert check.check_show('multimedia_directory_sample S00E00') is True


def test1_filemapper_check_show():
    assert check.check_show('multimedia_directory_sample S00E00.mkv') is True


# Multimedia Film Directory/File Tests
def test0_filemapper_check_film():
    assert check.check_film_type('multimedia_directory_sample (1950)') is True


def test1_filemapper_check_film():
    assert check.check_film_type('multimedia_directory_sample (1250)') is False


def test2_filemapper_check_film():
    assert check.check_film_type('multimedia_directory_sample (1950).mkv') is True


#Multimedia Season Directory Tests
def test0_filemapper_check_season_directory():
    assert check.check_season_directory('multimedia_directory_sample Season 1') is True


def test1_filemapper_check_season_directory():
    assert check.check_season_directory('multimedia_directory_sample (Season 1)') is True


def test2_filemapper_check_season_directory():
    assert check.check_season_directory('multimedia_directory_sample [Season 1]') is True


def test3_filemapper_check_season_directory():
    assert check.check_season_directory('multimedia_directory_sample S1') is True


def test4_filemapper_check_season_directory():
    assert check.check_season_directory('multimedia_directory_sample (S1)') is True


def test4_filemapper_check_season_directory():
    assert check.check_season_directory('multimedia_directory_sample [S1]') is True


#Unwanted File Tests
def test0_filemapper_check_unwanted():
    assert check.check_unwanted('nfo_sample.nfo') is True


def test1_filemapper_check_unwanted():
    assert check.check_unwanted('txt_sample.txt') is True


def test2_filemapper_check_unwanted():
    assert check.check_unwanted('com_sample.com') is True


#Complex Checking
#Main Show Directory Tests
def test0_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('multimedia_main_directory_show') is True


def test1_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('multimedia_main_directory_show 1080p') is True


def test2_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('multimedia_main_directory_show Season 0') is False


def test3_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('[HorribleSubs] multimedia_main_directory_show - 10') is False


def test4_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('[HorribleSubs] multimedia_main_directory_show x10') is False


def test5_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('[HorribleSubs] multimedia_main_directory_show Episode 10') is False


def test6_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('[HorribleSubs] multimedia_main_directory_show E10') is False


def test7_filemapper_check_main_directory_show():
    assert check.check_main_directory_show('multimedia_main_directory_show (1980)') is False


# Show Subtitles Tests
def test0_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample S01E01 (subtitles).srt') is True


def test1_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample subtitles.srt') is False


def test2_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('[HorribleSubs] multimedia_sample episode 1 subtitles.srt') is False


def test3_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample (1980) subtitles.srt') is False


def test4_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample S01E01 (subtitles).ass') is True


def test5_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample subtitles.ass') is False


def test6_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('[HorribleSubs] multimedia_sample episode 1 subtitles.ass') is False


def test7_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample (1980) subtitles.ass') is False


def test8_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample S01E01 (subtitles).sub') is True


def test9_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample subtitles.sub') is False


def test10_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('[HorribleSubs] multimedia_sample episode 1 subtitles.sub') is False


def test11_filemapper_check_show_subtitles():
    assert check.check_show_subtitles('multimedia_sample (1980) subtitles.sub') is False

#Show Directory Subtitles Tests
def test0_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('multimedia_sample_directory S01E01 subtitle') is True


def test1_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('multimedia_sample_directory S01E01 subtitles') is True


def test2_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('multimedia_sample_directory S01E01 subs') is False


def test3_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('multimedia_sample_directory S01E01 sub') is False


def test4_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('multimedia_sample_directory S01 sub') is False


def test5_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('multimedia_sample_directory (1980) subtitle') is False


def test6_filemapper_check_subtitles_directory_show():
    assert check.check_show_subtitles_directory('[HorribleSubs] multimedia_sample_directory subtitle') is False


#Anime Directory Tests
def test0_filemapper_check_anime_directory():
    assert check.check_anime_dir('[HorribleSubs] multimedia_sample_directory - 11') is True


def test1_filemapper_check_anime_directory():
    assert check.check_anime_dir('[HorribleSubs] multimedia_sample_directory E11') is True


def test2_filemapper_check_anime_directory():
    assert check.check_anime_dir('[HorribleSubs] multimedia_sample_directory Episode 11') is True


def test3_filemapper_check_anime_directory():
    assert check.check_anime_dir('[HorribleSubs] multimedia_sample_directory x11') is True


#Anime Show Test
def test0_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample - 11.mkv') is True


def test1_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample E11.mkv') is True


def test2_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample Episode 11.mkv') is True


def test3_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample x11.mkv') is True


def test4_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample - 11.mp4') is True


def test5_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample E11.mp4') is True


def test6_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample Episode 11.mp4') is True


def test7_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample_directory Episode 11') is False


def test8_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample_directory x11') is False


def test9_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample_directory E11') is False


def test10_filemapper_check_anime_show():
    assert check.check_anime_show('[HorribleSubs] multimedia_sample_directory - 11') is False


def test11_filemapper_check_anime_show():
    assert check.check_anime_show('multimedia_sample_directory Season 0') is False


def test12_filemapper_check_anime_show():
    assert check.check_anime_show('multimedia_sample_directory S0E0') is False


def test13_filemapper_check_anime_show():
    assert check.check_anime_show('multimedia_sample_directory (1980)') is False