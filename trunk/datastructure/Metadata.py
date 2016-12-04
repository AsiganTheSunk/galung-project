#!/usr/bin/python

class Metada ():
    def __init__(self, name=None, year=None, ename=None, season=None, episode=None, quality=None, film_flag=None, language=None,
          subtitle=None, uploader=None,  source=None, extension=None, file_flag=None):

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
        self.file_flag = file_flag

    def extended_metadata(self,director=None, actors=None, genre=None, duration=None, chapters=None):
        return ExtendedMetada(self.name, self.ename, self.season, self.episode, self.quality, self.extension, self.uploader,
                              self.source, self.year, self.film_flag, self.language, self.subtitle, self.file_flag,
                              director=director, actors=actors, genre=genre, duration= duration, chapters=chapters)
    def get_name(self):
        return self.name

    def get_ename(self):
        return self.ename

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def set_name(self, name):
        self.name = name

    def set_ename(self, ename):
        self.ename = ename

    def set_season(self, season):
        self.season = season

    def get_episode(self, episode):
        return self.episode

class ExtendedMetada (Metada):

    def __init__ (self, name=None, year=None, ename=None, season=None, episode=None, quality=None, film_flag=None,
                  language=None, subtitle=None, uploader=None,  source=None, extension=None, file_flag=None,
                  director=None, actors=None, genre=None, duration= None, chapters=None):

        self.director = director
        self.actors = actors
        self.genre = genre
        self.duration = duration
        self.chapter = duration

        Metada.__init__ (self, name=name, year=year, ename=ename, season=season, episode=episode, quality=quality, film_flag=film_flag, language=language,
          subtitle=subtitle, uploader=uploader,  source=source, extension=extension, file_flag=file_flag)

