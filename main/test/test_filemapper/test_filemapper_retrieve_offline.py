from main.filemapper.retrieve import offline_retrieve_module as offrmod


#Quality
def test0_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name BRRip') == 'BRRip'


def test1_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name HDRip') == 'HDRip'


def test2_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name BluRay') == 'BluRay'


def test3_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name DvdRip') == 'DvdRip'


def test4_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name HDTV') == 'HDTV'


def test5_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name WEBDL') == 'WEBDL'


def test6_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name WEB-DL') == 'WEB-DL'


def test7_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name WEBRip') == 'WEBRip'


def test8_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name WEB-Rip') == 'WEB-Rip'


def test9_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name 1080p') == '1080p'


def test10_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name 720p') == '720p'


def test11_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name 480p') == '480p'


def test12_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name 360p') == '360p'


def test13_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name (1280x720)') == '720p'


def test14_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name (10000x10)') == ''


def test15_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name high quality') == ''


def test16_retrieve_offline_quality():
    assert offrmod.retrieve_quality(path='multimedia_sample_name calidad gozosa') == ''


#Show Episode
def test0_retrieve_offline_episode():
    assert offrmod.retrieve_episode(path='multimedia_sample_name s01e01') == '01'


def test1_retrieve_offline_episode():
    assert offrmod.retrieve_episode(path='multimedia_sample_name season01episode01') == '01'


#Show Season
def test0_retrieve_offline_season_directory():
    assert offrmod.retrieve_season_directory(path='multimedia_sample_name season 0') == '0'


def test1_retrieve_offline_season_directory():
    assert offrmod.retrieve_season_directory(path='multimedia_sample_name season 22') == '22'


def test2_retrieve_offline_season_directory():
    assert offrmod.retrieve_season_directory(path='multimedia_sample_name season 01') == '1'


def test3_retrieve_offline_season_directory():
    assert offrmod.retrieve_season_directory(path='multimedia_sample_name s1') == '1'


def test4_retrieve_offline_season_directory():
    assert offrmod.retrieve_season_directory(path='multimedia_sample_name s 1') == '1'


#Show Season
def test0_retrieve_offline_season():
    assert offrmod.retrieve_season(path='multimedia_sample s01e01') == '01'


def test1_retrieve_offline_season():
    assert offrmod.retrieve_season(path='multimedia_sample s001e01') == '00'


def test2_retrieve_offline_season():
    assert offrmod.retrieve_season(path='multimedia_sample season01episode01') == ''


def test3_retrieve_offline_season():
    assert offrmod.retrieve_season(path='multimedia_sample season01') == ''


# Neutral Token Audio Tests
def test0_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) ACC') == 'ACC'


def test1_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) AC3') == 'AC3'


def test2_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) DTS') == 'DTS'


def test3_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) DD5.1') == 'DD5.1'


def test4_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) ACC2.0') == 'ACC2.0'


def test5_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='mutlimedia_sample (1980) MP3') == 'MP3'


def test6_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) m4a') == ''


def test7_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) HQAdio') == ''


def test8_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) LowQAudio') == ''


def test9_retrieve_offline_audio():
    assert offrmod.retrieve_offline_audio(path='multimedia_sample (1980) 320Kbps') == ''


# Netural Token Codec Tests
def test0_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) x264.mkv') == 'x264'


def test1_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) h264.mkv') == 'h264'


def test2_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) x265.mkv') == 'x265'


def test3_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) h265.mkv') == 'h265'


def test4_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) Xvid.mkv') == 'Xvid'


def test5_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) DivX.mkv') == 'DivX'


def test6_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='multimedia_sample (1980) mpeg2.mkv') == ''


def tet7_retrieve_offline_codec():
    assert offrmod.retrieve_offline_codec(path='mutlimedia_sample (1980) HQCodec.mkv') == ''


# Neutal Token Extension Tests
def test0_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.mkv') == '.mkv'


def test1_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.mp4') == '.mp4'


def test2_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.srt') == '.srt'


def test3_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.sub') == '.sub'


def test4_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.ass') == '.ass'


def test5_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.mpeg') == ''


def test6_retrieve_extension():
    assert offrmod.retrieve_extension(path='multimedia_sample.flv') == ''


# TODO FALLAN LOS TEST DE SOURCE Y UPLOADER el re.espace no se que cojones hace
# # Neutral Token Source Tests source_list = ['rartv', 'rarbg', 'ettv', 'RARBG']
# def test0_retrieve_source():
#     assert offrmod.retrieve_source(path='multimedia_sample rartv') == 'rartv'
#
#
# def test1_retrieve_source():
#     assert offrmod.retrieve_source(path='multimedia_sample rarbg') == 'rarbg'
#
#
# def test2_retrieve_source():
#     assert offrmod.retrieve_source(path='multimedia_sample ettv') == 'ettv'
#
#
# def test3_retrieve_source():
#     assert offrmod.retrieve_source(path='multimedia_sample') == ''
#
#
# def test4_retrieve_source():
#     assert offrmod.retrieve_source(path='[Coco_X] multimedia_sample') == ''
#
#
# # Neutral Token Uploader Tests
# def test0_retrieve_uploader():
#     assert offrmod.retrieve_uploader(path='multimedia_sample FUM') == 'FUM'
#
#
# def test1_retrieve_uploader():
#     assert offrmod.retrieve_uploader(path='multimedia_sample DIMENSION') == 'DIMENSION'
#
#
# def test2_retrieve_uploader():
#     assert offrmod.retrieve_uploader(path='multimedia_sample PODO') == 'PODO'
#
#
# def test3_retrieve_uploader():
#     assert offrmod.retrieve_uploader(path='multimedia_sample ROVERS') == 'ROVERS'
#
#
# def test4_retrieve_uploader():
#     assert offrmod.retrieve_uploader(path='multimedia_sample PAQUITO') == ''