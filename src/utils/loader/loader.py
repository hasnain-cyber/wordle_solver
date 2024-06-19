class Loader:
    def __init__(self, filepath: str):
        self.filepath = filepath

        self.data = None

    def load(self, filepath: str):
        raise NotImplementedError('load() method must be implemented')

    def get(self):
        if self.data is None:
            self.load(self.filepath)
        return self.data
