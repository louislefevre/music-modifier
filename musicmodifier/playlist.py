from mutagen.easyid3 import EasyID3
from musicmodifier.utilities import file_iterator
from musicmodifier.artist import Artist
from musicmodifier.album import Album
from musicmodifier.track import Track

class Playlist:
    _counter = 0

    def __init__(self, dir):
        self._name = 'playlist'
        self._dir = dir
        self._all_artists = []
        Playlist._counter += 1
        self._create_playlist()

    def _create_playlist(self):
        file_paths = file_iterator(self._dir)
        for path in file_paths:
            self._create_info(path)

    def _create_info(self, path):
        audio = EasyID3(path)
        title = ''.join(audio['title'])
        artist = ''.join(audio['artist'])
        album = ''.join(audio['album'])
        track = {'title':title, 'artist':artist, 'album':album}
        self._create_artist(track)

    def _create_artist(self, track):
        artist_name = track.get('artist')
        artist = self._check_exists(artist_name, self.get_artists())
        if not artist:
            artist = Artist(artist_name)
            self._add_artist(artist)
        self._create_album(track, artist)

    def _create_album(self, track, artist):
        album_name = track.get('album')
        album = self._check_exists(album_name, artist.get_albums())
        if not album:
            album = Album(album_name)
            artist.add_album(album)
        self._create_track(track, album)

    def _create_track(self, track, album):
        track_name = track.get('title')
        track = self._check_exists(track_name, album.get_tracks())
        if not track:
            track = Track(track_name)
            album.add_track(track)

    def _check_exists(self, name, array):
        for item in array:
            if item.get_name() == name:
                return item
        return None

    def _add_artist(self, artist):
        self._all_artists.append(artist)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_dir(self):
        return self._dir

    def get_artists(self):
        return self._all_artists

    @staticmethod
    def get_counter():
        return Playlist._counter
