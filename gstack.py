
class GStack():
    def __init__(self):
        self._data = []

    def size(self):
        return len(self._data)

    def pop(self):
        if(len(self._data)==0):
            return None
        else:
            return self._data.pop()

    def push(self, item):
        self._data.append(item)
