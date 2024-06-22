class WordDictLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

        self.data: dict[str, int] = {}
        self.total_freq = 0

    def get(self):
        if len(self.data) == 0:
            self.load(self.filepath)
        return self.data

    def load(self, filepath: str):
        self.data = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            # Skip the first line
            next(file)
            for line in file:
                word, freq = line.strip().split(',')
                self.data[word] = int(freq)
                self.total_freq += self.data[word]
