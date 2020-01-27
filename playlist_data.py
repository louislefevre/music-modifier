import os
from mutagen.easyid3 import EasyID3
from utilities import file_iterator

class Playlist:
    _counter = 0
    def __init__(self):
        self.name = 'playlist'
        self.all_artists = []
        Playlist._counter += 1
    def get_name(self):
        return self.name
    def add_name(self, name):
        self.name = name
    def add_artist(self, artist):
        self.all_artists.append(artist)
    def get_artists(self):
        return self.all_artists
    def get_counter():
        return Playlist._counter

class Artist:
    _counter = 0
    def __init__(self, name):
        self.name = name
        self.albums = []
        Artist._counter += 1
    def get_name(self):
        return self.name
    def get_albums(self):
        return self.albums
    def add_album(self, album):
        self.albums.append(album)
    @staticmethod
    def get_counter():
        return Artist._counter

class Album:
    _counter = 0
    def __init__(self, name):
        self.name = name
        self.tracks = []
        Album._counter += 1
    def get_name(self):
        return self.name
    def get_tracks(self):
        return self.tracks
    def add_track(self, track):
        self.tracks.append(track)
    @staticmethod
    def get_counter():
        return Album._counter

class Track:
    _counter = 0
    def __init__(self, name):
        self.name = name
        Track._counter += 1
    def get_name(self):
        return self.name
    @staticmethod
    def get_counter():
        return Track._counter

def new_playlist(path):
    file_paths = file_iterator(path)
    playlist = Playlist()
    for file_path in file_paths:
        track = get_track(file_path, playlist)
        create_artist(track, playlist)
    return playlist

def get_track(file_path, playlist):
    audio = EasyID3(file_path)
    title = ''.join(audio['title'])
    artist = ''.join(audio['artist'])
    album = ''.join(audio['album'])
    track_info = {'title':title, 'artist':artist, 'album':album}
    return track_info

def create_artist(track, playlist):
    artist_name = track.get('artist')
    artist = check_exists(artist_name, playlist.get_artists())
    if not artist:
        artist = Artist(artist_name)
        playlist.add_artist(artist)
    create_album(track, artist)

def create_album(track, artist):
    album_name = track.get('album')
    album = check_exists(album_name, artist.get_albums())
    if not album:
        album = Album(album_name)
        artist.add_album(album)
    create_track(track, album)

def create_track(track, album):
    track_name = track.get('title')
    track = check_exists(track_name, album.get_tracks())
    if not track:
        track = Track(track_name)
        album.add_track(track)

def check_exists(name, array):
    for item in array:
        if item.get_name() == name:
            return item
    return None
