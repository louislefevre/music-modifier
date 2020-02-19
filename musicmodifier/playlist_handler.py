import os
import shutil
from musicmodifier.utilities import file_iterator, request_permission, input_directory, EXTENSIONS
from musicmodifier.playlist import Playlist
from musicmodifier.artist import Artist
from musicmodifier.album import Album
from musicmodifier.track import Track


def display_playlist(playlist):
    text = _get_playlist(playlist)
    print(text)


def convert_playlist(playlist):
    text = _get_playlist(playlist)
    file = open(playlist.get_name() + '.txt', 'w')
    file.write(text)
    file.close()


def combine_playlist(playlist):
    src_directory = input_directory()
    src_playlist = Playlist(src_directory)
    dest_playlist = playlist
    if not request_permission():
        return
    _compare_playlists(src_playlist, dest_playlist)


def remove_numbers(playlist):
    directory = playlist.get_directory()
    _search_directories(directory)


def _get_playlist(playlist):
    text = ''
    artists = playlist.get_artists()
    for artist in artists:
        text += '-' + artist.get_name() + '\n'
        for album in artist.get_albums():
            text += ' -' + album.get_name() + '\n'
            for track in album.get_tracks():
                text += '  -' + track.get_name() + '\n'
        text += '\n'
    text += 'Artists: ' + str(Artist.get_counter()) + '\n'
    text += 'Albums: ' + str(Album.get_counter()) + '\n'
    text += 'Tracks: ' + str(Track.get_counter()) + '\n'
    return text


def _compare_playlists(src, dest):
    dest_directory = dest.get_directory()
    src_directory = src.get_directory()
    for src_artist in src.get_artists():
        for src_album in src_artist.get_albums():
            for src_track in src_album.get_tracks():
                artist_path = dest_directory + '\\' + src_artist.get_name()
                album_path = artist_path + '\\' + src_album.get_name()
                track_path = album_path + '\\' + src_track.get_name() + EXTENSIONS
                src_path = src_directory + '\\' + src_track.get_name() + EXTENSIONS
                dest_path = track_path
                if not os.path.exists(artist_path):
                    _create_folder(artist_path)
                if not os.path.exists(album_path):
                    _create_folder(album_path)
                if not os.path.exists(track_path):
                    _move_file(src_path, dest_path)
                    print(f'Moving "{src_track.get_name()}" to "{src_artist.get_name()}\\{src_album.get_name()}".')
                else:
                    print(f'The track "{src_track.get_name()}" already exists.')


def _create_folder(path):
    os.mkdir(path)


def _move_file(src_path, dest_path):
    try:
        shutil.move(src_path, dest_path)
    except FileNotFoundError:
        print(f'Failed to find "{src_path}".')


def _search_directories(directory):
    file_paths = file_iterator(directory)
    file_changes = []
    for path in file_paths:
        file_dir, file_name = os.path.split(path)
        if file_name[0:2].isdigit() and file_name[2].isspace():
            new_name = file_name[3:]
            new_path = os.path.join(file_dir, new_name)
            file_info = {'old_name': file_name, 'new_name': new_name, 'old_path': path, 'new_path': new_path}
            file_changes.append(file_info)
    _validate_files(file_changes)


def _validate_files(file_changes):
    if not file_changes:
        print('No files need to be renamed.')
        return
    else:
        _list_changes(file_changes)
    if not request_permission():
        return
    for item in file_changes:
        _rename_files(item)


def _list_changes(file_changes):
    for item in file_changes:
        print('')
        print(f'"{item.get("old_name")}" will be renamed to "{item.get("new_name")}"')


def _rename_files(item):
    try:
        os.rename(item.get('old_path'), item.get('new_path'))
        print(f'Renamed "{item.get("old_name")}" to "{item.get("new_name")}"')
    except FileNotFoundError:
        print('')
        print(f'Could not find file "{item.get("old_name")}", skipping...')
    except FileExistsError:
        print('')
        print(f'File name "{item.get("new_name")}" already exists, skipping...')
