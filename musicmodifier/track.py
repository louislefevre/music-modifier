class Track:
    _counter = 0

    def __init__(self, name, path):
        self._name = name
        self._path = path
        Track._counter += 1

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    @staticmethod
    def get_counter():
        return Track._counter
