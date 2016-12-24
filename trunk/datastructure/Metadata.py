# glob, fmatch


class Metadata:
    def __init__(self, name=None, year=None, ename=None, season=None, episode=None, quality=None, film_flag=None, language=None,
                 subtitle=None, uploader=None,  source=None, extension=None, file_flag=None, audio=None, codec=None):

        self.name = name
        self.ename = ename
        self.season = season
        self.episode = episode
        self.quality = quality
        self.extension = extension
        self.uploader = uploader
        self.source = source
        self.year = year
        self.film_flag = film_flag
        self.language = language
        self.subtitle = subtitle
        self.audio = audio
        self.codec = codec
        self.file_flag = file_flag

    def extended_metadata(self, director=None, actors=None, genre=None, duration=None, chapters=None):
        return ExtendedMetada(self.name, self.ename, self.season, self.episode, self.quality, self.extension, self.uploader,
                              self.source, self.year, self.film_flag, self.language, self.subtitle, self.file_flag,
                              director=director, actors=actors, genre=genre, duration=duration, chapters=chapters)

    def get_name(self):
        return self.name

    def get_ename(self):
        return self.ename

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def get_quality(self):
        return self.quality

    def get_extension(self):
        return self.extension

    def get_source(self):
        return self.source

    def get_year(self):
        return self.year

    def get_film_flag(self):
        return self.film_flag

    def get_language(self):
        return self.language

    def get_subtitle(self):
        return self.subtitle

    def get_uploader(self):
        return self.uploader

    def set_name(self, name):
        self.name = name

    def set_ename(self, ename):
        self.ename = ename

    def set_episode(self, episode):
        self.episode = episode

    def set_season(self, season):
        self.season = season

    def set_quality(self, quality):
        self.quality = quality

    def set_extension(self, extension):
        self.extension = extension

    def set_source(self, source):
        self.source = source

    def set_year(self, year):
        self.year = year

    def set_film_flag(self, film_tag):
        self.film_flag = film_tag

    def set_language(self, language):
        self.language = language

    def set_subtitle(self, subtitle):
        self.subtitle = subtitle

    def set_uploader(self, uploader):
        self.uploader = uploader

    def set_audio(self, audio):
        self.audio = audio

    def set_codec(self, codec):
        self.codec = codec


class ExtendedMetada (Metadata):
    def __init__(self, name=None, year=None, ename=None, season=None, episode=None, quality=None, film_flag=None,
                 language=None, subtitle=None, uploader=None,  source=None, extension=None, file_flag=None,
                 director=None, actors=None, genre=None, duration=None, chapters=None):

        self.director = director
        self.actors = actors
        self.genre = genre
        self.duration = duration
        self.chapters = chapters

        Metadata.__init__(self, name=name, year=year, ename=ename, season=season, episode=episode, quality=quality,
                          film_flag=film_flag, language=language, subtitle=subtitle, uploader=uploader,  source=source,
                          extension=extension, file_flag=file_flag)

    def get_director(self):
        return self.director

    def get_actors(self):
        return self.actors

    def get_genre(self):
        return self.genre

    def get_duration(self):
        return self.duration

    def get_chapters(self):
        return self.chapters

    def set_director(self, director):
        self.director = director

    def set_actors(self, actors):
        self.actors = actors

    def set_genre(self, genre):
        self.genre = genre

    def set_duration(self, duration):
        self.duration = duration

    def set_chapters(self, chapters):
        self.chapters = chapters
