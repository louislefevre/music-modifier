import sys
from numbers_remover import search_directories
from files_viewer import display_all_artists
from files_viewer import file_to_text

def print_features():
    print('-----------Music Modifier-----------')
    print('RemoveNumbers - Removes numbers at the beginning of song names.')
    print('ShowMusic - View all the artists, albums and tracks.')
    print('ToText - Write a log of your entire playlist to a text file.')
    print('Exit - Terminates the program.')
    print('------------------------------------')

def main():
    #path = sys.argv[1] # Removed for testing
    path = 'D:\Libraries\Music\iTunes\iTunes Media\MusicTest'
    print_features()
    while(True):
        user_input = input('Select a feature: ').lower()
        if user_input == 'removenumbers':
            search_directories(path)
        elif user_input == 'showmusic':
            display_all_artists(path)
            break
        elif user_input == 'totext':
            file_to_text(path)
            break
        elif user_input == 'exit':
            break
        else:
            print('Invalid input - enter one of the feature names listed above.')
