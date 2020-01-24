import os
from mutagen.easyid3 import EasyID3
from operator import itemgetter


################################################################################
def searchDirectories(path):
    file_types = ('.mp3', '.m4a')
    file_changes = []
    for sub_dir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_types) and file[0:2].isdigit() and file[2].isspace():
                new_file = file[3:]
                old_path = os.path.join(sub_dir, file)
                new_path = os.path.join(sub_dir, new_file)
                if os.path.exists(new_path):
                    print(f'File name "{new_file}" already exists, skipping... ({new_path})')
                else:
                    file_changes.append([file, new_file, old_path, new_path])
    requestPermission(file_changes)

def requestPermission(file_changes):
    if not file_changes:
        print('No files need to be renamed.')
        return
    listChanges(file_changes)
    while True:
        request = input('The files listed will be changed. Do you want to proceed? [yes/no]').lower()
        if request == 'yes':
            break;
        elif request == 'no':
            print('Program terminating...')
            return
        else:
            print('Invalid input - please enter "yes" or "no".')
    renameFiles(file_changes)

def listChanges(file_changes):
    for item in file_changes:
        print(f'"{item[0]}" will be renamed to "{item[1]}"')

def renameFiles(file_changes):
    for item in file_changes:
        try:
            os.rename(item[2], item[3])
            print(f'Renamed "{item[0]}" to "{item[1]}"')
        except FileNotFoundError:
            print(f'Could not find file {item[0]}, skipping...')

################################################################################
class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
    def getName(self):
        return self.name
    def getAlbums(self):
        return self.albums
    def addAlbum(self, album):
        self.albums.append(album)

class Album:
    def __init__(self, name):
        self.name = name
        self.tracks = []
    def getName(self):
        return self.name
    def getTracks(self):
        return self.tracks
    def addTrack(self, track):
        self.tracks.append(track)

class Track:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

def getAllArtists(path):
    file_types = ('.mp3')
    all_artists = []
    for sub_dir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_types):
                file_path = os.path.join(sub_dir, file)
                getArtistData(file_path, all_artists)
    printAllArtists(all_artists)

def getArtistData(file_path, all_artists):
    audio = EasyID3(file_path)
    title = ''.join(audio['title'])
    artist = ''.join(audio['artist'])
    album = ''.join(audio['album'])
    track_info = {'title':title, 'artist':artist, 'album':album}
    createArtist(track_info, all_artists)

def createArtist(track_info, all_artists):
    artist_name = track_info.get('artist')
    for artist in all_artists:
        if artist.getName() == artist_name:
            createAlbum(track_info, artist)
            return
    artist = Artist(artist_name)
    all_artists.append(artist)
    createAlbum(track_info, artist)

def createAlbum(track_info, artist):
    album_name = track_info.get('album')
    for album in artist.getAlbums():
        if album.getName() == album_name:
            createTrack(track_info, album)
            return
    album = Album(album_name)
    artist.addAlbum(album)
    createTrack(track_info, album)

def createTrack(track_info, album):
    track_name = track_info.get('title')
    for track in album.getTracks():
        if track.getName() == track_name:
            return
    track = Track(track_name)
    album.addTrack(track)

def printAllArtists(artists):
    for artist in artists:
        print('--' + artist.getName())
        for album in artist.getAlbums():
            print(' -' + album.getName())
            for track in album.getTracks():
                print('  -' + track.getName())
        print('')

################################################################################
def printFeatures():
    print('-----Welcome to Music Modifier!-----')
    print('RemoveNumbers - Removes numbers at the beginning of song names.')
    print('Exit - Terminates the program.')
    print('------------------------------------')

def main():
    path = 'D:\Libraries\Music\iTunes\iTunes Media\Music'
    printFeatures()
    while(True):
        user_input = input('Select a feature: ').lower()
        if user_input == 'removenumbers':
            searchDirectories(path)
        elif user_input == 't':
            getAllArtists(path)
            break
        elif user_input == 'exit':
            break
        else:
            print('Invalid input - enter one of the feature names listed above.')

if __name__ == '__main__':
    main()


# Retrieve the title of the song and use that instead?

# Create functionality to export music data to text file (organised by bands, albums, etc)

# Before running getArtistData, run a check to ensure all files have the relevant information.

# Add functionality to automatically organise new music. For example, give it a song with the band
# the album, position, etc, and it will automatically move it to the correct location. If the location
# doesnt exist, it will create it.

# Combinate file search functions to a single function, with different methods being passed or something.
