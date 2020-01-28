import os

EXTENSIONS = '.mp3'

def extensions():
    return EXTENSIONS

def file_iterator(path):
    file_types = ('.mp3')
    file_paths = []
    for sub_dir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_types):
                full_path = os.path.join(sub_dir, file)
                file_paths.append(full_path)
    return file_paths

def request_permission():
    while True:
        request = input('Do you want to proceed? [yes/no]').lower()
        if request == 'yes':
            return True
        elif request == 'no':
            print('Process cancelled, returning to menu...')
            return False
        else:
            print('Invalid input - please enter "yes" or "no".')

def input_path():
    while True:
        path = input('Enter the path: ')
        if os.path.isdir(path):
            break
        elif path == 'exit':
            quit_program()
        else:
            print('Invalid path.')
    return path

def quit_program():
    print('Thank you for using Music Modifier, goodbye...')
    quit()
