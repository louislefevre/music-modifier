import os
from mutagen.easyid3 import EasyID3
from utilities import file_iterator

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
    def get_name(self):
        return self.name
    def get_albums(self):
        return self.albums
    def add_album(self, album):
        self.albums.append(album)

class Album:
    def __init__(self, name):
        self.name = name
        self.tracks = []
    def get_name(self):
        return self.name
    def get_tracks(self):
        return self.tracks
    def add_track(self, track):
        self.tracks.append(track)

class Track:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

def display_all_artists(path):
    artists = get_all_artists(path)
    for artist in artists:
        print('--' + artist.get_name())
        for album in artist.get_albums():
            print(' -' + album.get_name())
            for track in album.get_tracks():
                print('  -' + track.get_name())
        print('')

def get_all_artists(path):
    file_paths = file_iterator(path)
    all_artists = []
    for file_path in file_paths:
        get_artist_data(file_path, all_artists)
    return all_artists

def get_artist_data(file_path, all_artists):
    audio = EasyID3(file_path)
    title = ''.join(audio['title'])
    artist = ''.join(audio['artist'])
    album = ''.join(audio['album'])
    track_info = {'title':title, 'artist':artist, 'album':album}
    create_artist(track_info, all_artists)

def create_artist(track_info, all_artists):
    artist_name = track_info.get('artist')
    for artist in all_artists:
        if artist.get_name() == artist_name:
            create_album(track_info, artist)
            return
    artist = Artist(artist_name)
    all_artists.append(artist)
    create_album(track_info, artist)

def create_album(track_info, artist):
    album_name = track_info.get('album')
    for album in artist.get_albums():
        if album.get_name() == album_name:
            create_track(track_info, album)
            return
    album = Album(album_name)
    artist.add_album(album)
    create_track(track_info, album)

def create_track(track_info, album):
    track_name = track_info.get('title')
    for track in album.get_tracks():
        if track.get_name() == track_name:
            return
    track = Track(track_name)
    album.add_track(track)
