from src.utils.loader.loader import Loader


class WordDictLoader(Loader):
    def __init__(self, filepath: str):
        super().__init__(filepath)

        self.total_freq = 0

    def load(self, filepath: str):
        self.data = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            # Skip the first line
            next(file)
            for line in file:
                word, freq = line.strip().split(',')
                self.data[word] = int(freq)
                self.total_freq += self.data[word]

    def get_total_freq(self):
        if self.data is None:
            self.load(self.filepath)
        return self.total_freq
