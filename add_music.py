import os
import shutil
from playlist import Playlist
from files_viewer import display_playlist
from utilities import request_permission, input_dir, extensions

def add_tracks(dest_dir):
    src_dir = input_dir()
    src = Playlist(src_dir)
    dest = Playlist(dest_dir)
    if not request_permission():
        return
    compare_playlists(src, dest)

def compare_playlists(src, dest):
    dest_dir = dest.get_dir()
    src_dir = src.get_dir()
    for src_artist in src.get_artists():
            for src_album in src_artist.get_albums():
                    for src_track in src_album.get_tracks():
                        artist_path = dest_dir + '\\' + src_artist.get_name()
                        album_path = artist_path + '\\' + src_album.get_name()
                        track_path = album_path + '\\' + src_track.get_name() + extensions()
                        src_path = src_dir + '\\' + src_track.get_name() + extensions()
                        dest_path = track_path
                        if not os.path.exists(artist_path):
                            create_folder(artist_path)
                        if not os.path.exists(album_path):
                            create_folder(album_path)
                        if not os.path.exists(track_path):
                            move_file(src_path, dest_path)
                            print(f'Moving "{src_track.get_name()}" to "{src_artist.get_name()}\\{src_album.get_name()}".')
                        else:
                            print(f'The track "{src_track.get_name()}" already exists.')

def create_folder(path):
    os.mkdir(path)

def move_file(src_path, dest_path):
    try:
        shutil.move(src_path, dest_path)
    except FileNotFoundError:
        print(f'Failed to find "{src_path}".')
