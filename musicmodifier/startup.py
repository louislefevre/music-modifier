from musicmodifier.numbers_remover import search_directories
from musicmodifier.utilities import quit_program
from musicmodifier.playlist_handler import display_playlist, convert_playlist, combine_playlist
from musicmodifier.playlist import Playlist


def print_features():
    print('----------------------Music Modifier----------------------')
    print('Playlist - View all the artists, albums and tracks.')
    print('Text - Write a log of your entire playlist to a text file.')
    print('Add - Takes a source folder and adds its contents into music folder.')
    print('Remove - Removes numbers at the beginning of song names.')
    print('Exit - Terminates the program.')
    print('')
    print('Begin by entering the path containing your playlist, and then')
    print('select a feature by typing its name in as a command.')
    print('----------------------------------------------------------')


def main():
    print_features()
    directory = 'D:\Libraries\Music\iTunes\iTunes Media\Testing\MusicTest'  # input_directory()
    playlist = Playlist(directory)
    while True:
        user_input: str = input('Select a feature: ').lower()
        if user_input == 'playlist':
            display_playlist(playlist)
        elif user_input == 'text':
            convert_playlist(playlist)
        elif user_input == 'add':
            combine_playlist(playlist)
        elif user_input == 'remove':
            search_directories(directory)
        elif user_input == 'exit':
            quit_program()
        else:
            print('Invalid input - enter one of the feature names listed above.')



