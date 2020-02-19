class Album:
    _counter = 0

    def __init__(self, name):
        self._name = name
        self._tracks = []
        Album._counter += 1
        
    def get_name(self):
        return self._name

    def get_tracks(self):
        return self._tracks

    def add_track(self, track):
        self._tracks.append(track)

    @staticmethod
    def get_counter():
        return Album._counter
