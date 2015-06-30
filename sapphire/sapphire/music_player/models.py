from django.db import models
from django.contrib import admin
from durationfield.db.models.fields.duration import DurationField


class Song(models.Model):
    title = models.CharField(max_length=142)
    artist = models.CharField(max_length=142)
    album = models.CharField(max_length=142)
    lenght = DurationField()
    rating = models.IntegerField()
    track_num = models.IntegerField()
    path_to_song = 

    def __unicode__(self):
        return self.title


class Collection(models.Model):
    song_list = {}

    def add_song(self, song):
        self.song_list[song.title] = song

    def rm_song(self, song):
        del self.song_list[song.title]


class Album(Collection):
    title = models.CharField(max_length=142)

    def __unicode__(self):
        return self.title


class Artist(Collection):
    scene_name = models.CharField(max_length=142)
    fist_name = models.CharField(max_length=142)
    last_name = models.CharField(max_length=142)
    album_list = {}

    def __unicode__(self):
        return self.scene_name


class Playlist(Collection):
    title = models.CharField(max_length=142)

    def __unicode__(self):
        return self.title


admin.site.register(Song, Album, Artist, Playlist)
