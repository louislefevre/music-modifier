from playlist_data import new_playlist
from playlist_data import Playlist
from playlist_data import Artist
from playlist_data import Album
from playlist_data import Track

def display_all_artists(path):
    playlist = new_playlist(path)
    artists = playlist.get_artists()
    for artist in artists:
        print('-' + artist.get_name())
        for album in artist.get_albums():
            print(' -' + album.get_name())
            for track in album.get_tracks():
                print('  -' + track.get_name())
        print('')
    display_counters()

def display_counters():
    print('Artists: ' + str(Artist.get_counter()))
    print('Albums: ' + str(Album.get_counter()))
    print('Tracks: ' + str(Track.get_counter()))

def file_to_text(path):
    playlist = new_playlist(path)
    artists = playlist.get_artists()
    file = create_file(playlist)
    for artist in artists:
        file.write('-' + artist.get_name() + '\n')
        for album in artist.get_albums():
            file.write(' -' + album.get_name() + '\n')
            for track in album.get_tracks():
                file.write('  -' + track.get_name() + '\n')
        file.write('\n')
    file.close()

def create_file(playlist):
    name = input('Enter playlist name (leave blank for default): ').strip()
    if not name:
        name = playlist.get_name()
    file = open(name + '.txt', 'w')
    return file
