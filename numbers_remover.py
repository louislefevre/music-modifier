import os
from utilities import file_iterator

def search_directories(path):
    file_paths = file_iterator(path)
    file_changes = []
    for file_path in file_paths:
        file_dir, file_name = os.path.split(file_path)
        if file_name[0:2].isdigit() and file_name[2].isspace():
            new_name = file_name[3:]
            new_path = os.path.join(file_dir, new_name)
            file_info = {'old_name': file_name, 'new_name': new_name, 'old_path': file_path, 'new_path': new_path}
            file_changes.append(file_info)
    rename_files(file_changes)

def rename_files(file_changes):
    if not file_changes:
        print('No files need to be renamed.')
        return
    if not request_permission(file_changes):
        return
    for item in file_changes:
        try:
            os.rename(item.get('old_path'), item.get('new_path'))
            print(f'Renamed "{item.get("old_name")}" to "{item.get("new_name")}"')
        except FileNotFoundError:
            print('')
            print(f'Could not find file "{item.get("old_name")}", skipping...')
        except FileExistsError:
            print('')
            print(f'File name "{item.get("new_name")}" already exists, skipping...')

def request_permission(file_changes):
    list_changes(file_changes)
    while True:
        request = input('The files listed will be changed. Do you want to proceed? [yes/no]').lower()
        if request == 'yes':
            return True
        elif request == 'no':
            print('Process cancelled, returning to menu...')
            return False
        else:
            print('Invalid input - please enter "yes" or "no".')

def list_changes(file_changes):
    for item in file_changes:
        print('')
        print(f'"{item.get("old_name")}" will be renamed to "{item.get("new_name")}"')
