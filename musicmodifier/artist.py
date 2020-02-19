class Artist:
    _counter = 0
    
    def __init__(self, name, path):
        self._name = name
        self._path = path
        self._albums = []
        Artist._counter += 1

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_albums(self):
        return self._albums

    def add_album(self, album):
        self._albums.append(album)

    @staticmethod
    def get_counter():
        return Artist._counter
