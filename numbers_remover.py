import os

def search_directories(path):
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
    request_permission(file_changes)

def request_permission(file_changes):
    if not file_changes:
        print('No files need to be renamed.')
        return
    list_changes(file_changes)
    while True:
        request = input('The files listed will be changed. Do you want to proceed? [yes/no]').lower()
        if request == 'yes':
            break;
        elif request == 'no':
            print('Process cancelled, returning to menu...')
            return
        else:
            print('Invalid input - please enter "yes" or "no".')
    rename_files(file_changes)

def list_changes(file_changes):
    for item in file_changes:
        print(f'"{item[0]}" will be renamed to "{item[1]}"')

def rename_files(file_changes):
    for item in file_changes:
        try:
            os.rename(item[2], item[3])
            print(f'Renamed "{item[0]}" to "{item[1]}"')
        except FileNotFoundError:
            print(f'Could not find file "{item[0]}", skipping...')
        except FileExistsError:
            print(f'File name "{item[0]}" already exists, skipping...')
