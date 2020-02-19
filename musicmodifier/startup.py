from musicmodifier.numbers_remover import search_directories
from musicmodifier.files_viewer import display_playlist, file_to_text
from musicmodifier.add_music import add_tracks
from musicmodifier.utilities import quit_program, input_directory


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
    directory = input_directory()  # 'D:\Libraries\Music\iTunes\iTunes Media\Testing\MusicTest'
    while():
        user_input: str = input('Select a feature: ').lower()
        if user_input == 'playlist':
            display_playlist(directory)
        elif user_input == 'text':
            file_to_text(directory)
        elif user_input == 'add':
            add_tracks(directory)
        elif user_input == 'remove':
            search_directories(directory)
        elif user_input == 'exit':
            quit_program()
        else:
            print('Invalid input - enter one of the feature names listed above.')
