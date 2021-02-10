# Though tempting to add persistence to the Journal object this can cause issues later when you
# need to make a change to how persistence works in general and each object is handline this in
# a duplicate manner.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(data_to_persist, filename):
        file = open(filename, 'w')
        file.write(str(data_to_persist))
        file.close

    def load(self, filename):
        pass

    def load_from_web(self, url):
        pass
