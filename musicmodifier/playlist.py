from mutagen.easyid3 import EasyID3
from musicmodifier.utilities import file_iterator
from musicmodifier.artist import Artist
from musicmodifier.album import Album
from musicmodifier.track import Track


class Playlist:
    _counter = 0

    def __init__(self, directory):
        self._name = 'playlist'
        self._directory = directory
        self._all_artists = []
        Playlist._counter += 1
        self._create_playlist()

    def _create_playlist(self):
        file_paths = file_iterator(self._directory)
        for path in file_paths:
            self._create_info(path)

    def _create_info(self, path):
        audio = EasyID3(path)
        title = ''.join(audio['title'])
        artist = ''.join(audio['artist'])
        album = ''.join(audio['album'])
        track_info = {'title': title, 'artist': artist, 'album': album, 'path': path}
        self._create_artist(track_info)

    def _create_artist(self, track_info):
        artist_name = track_info.get('artist')
        artist = self._check_exists(artist_name, self.get_artists())
        if not artist:
            artist_path = track_info.get('path').rsplit('\\', 2)[0]
            artist = Artist(artist_name, artist_path)
            self._add_artist(artist)
        self._create_album(track_info, artist)

    def _create_album(self, track_info, artist):
        album_name = track_info.get('album')
        album = self._check_exists(album_name, artist.get_albums())
        if not album:
            album_path = track_info.get('path').rsplit('\\', 1)[0]
            album = Album(album_name, album_path)
            artist.add_album(album)
        self._create_track(track_info, album)

    def _create_track(self, track_info, album):
        track_name = track_info.get('title')
        track = self._check_exists(track_name, album.get_tracks())
        if not track:
            track_path = track_info.get('path')
            track = Track(track_name, track_path)
            album.add_track(track)

    def _add_artist(self, artist):
        self._all_artists.append(artist)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_directory(self):
        return self._directory

    def get_artists(self):
        return self._all_artists

    @staticmethod
    def _check_exists(name, array):
        for item in array:
            if item.get_name() == name:
                return item
        return None

    @staticmethod
    def get_counter():
        return Playlist._counter
