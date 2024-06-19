from src.utils.loader.loader import Loader


class WordlistLoader(Loader):
    def load(self, filepath: str):
        self.data = []
        with open(filepath, 'r') as file:
            for line in file:
                self.data.append(line.strip())
