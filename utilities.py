import os

def file_iterator(path):
    file_types = ('.mp3')
    file_paths = []
    for sub_dir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_types):
                full_path = os.path.join(sub_dir, file)
                file_paths.append(full_path)
    return file_paths
