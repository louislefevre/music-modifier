class Track:
    _counter = 0

    def __init__(self, name):
        self._name = name
        Track._counter += 1

    def get_name(self):
        return self._name

    @staticmethod
    def get_counter():
        return Track._counter
