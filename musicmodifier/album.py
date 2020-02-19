class Album:
    _counter = 0

    def __init__(self, name, path):
        self._name = name
        self._path = path
        self._tracks = []
        Album._counter += 1
        
    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_tracks(self):
        return self._tracks

    def add_track(self, track):
        self._tracks.append(track)

    @staticmethod
    def get_counter():
        return Album._counter
