from musicmodifier.playlist import Playlist
from musicmodifier.playlist_handler import display_playlist, convert_playlist, combine_playlist, remove_numbers
from musicmodifier.utilities import quit_program


def print_features():
    print('----------------------Music Modifier----------------------')
    print('Display - Show all the artists, albums and tracks.')
    print('Convert - Create a text log of your entire playlist.')
    print('Combine - Takes a playlist and combines its contents with the original playlist.')
    print('Remove - Removes numbers at the beginning of track file names.')
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
        if user_input == 'display':
            display_playlist(playlist)
        elif user_input == 'convert':
            convert_playlist(playlist)
        elif user_input == 'add':
            combine_playlist(playlist)
        elif user_input == 'remove':
            remove_numbers(playlist)
        elif user_input == 'exit':
            quit_program()
        else:
            print('Invalid input - enter one of the feature names listed above.')
