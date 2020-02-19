import sys
from numbers_remover import search_directories
from files_viewer import display_playlist, file_to_text
from add_music import add_tracks
from utilities import input_path, quit_program

def print_features():
    print('----------------------Music Modifier----------------------')
    print('Playlist - View all the artists, albums and tracks.')
    print('ToText - Write a log of your entire playlist to a text file.')
    print('AddTracks - Takes a source folder and adds its contents into music folder.')
    print('RemoveNumbers - Removes numbers at the beginning of song names.')
    print('Exit - Terminates the program.')
    print('')
    print('Begin by entering the path containing your playlist, and then')
    print('select a feature by typing its name in as a command.')
    print('----------------------------------------------------------')

def main():
    print_features()
    dir = 'D:\Libraries\Music\iTunes\iTunes Media\Testing\MusicTest' # input_path()
    while(True):
        user_input = input('Select a feature: ').lower()
        if user_input == 'playlist':
            display_playlist(dir)
        elif user_input == 'totext':
            file_to_text(dir)
        elif user_input == 'addtracks':
            add_tracks(dir)
        elif user_input == 'removenumbers':
            search_directories(dir)
        elif user_input == 'exit':
            quit_program()
        else:
            print('Invalid input - enter one of the feature names listed above.')