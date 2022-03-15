import csv
from glob import escape

class CSV:
    def __init__(self, file):
        self._arr = self.build_arr(file)
    
    def __len__(self):
        return len(self._arr)

    def get(self, index):
        return self._arr[index]

    def build_arr(self, file):
        arr = []
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, escapechar='\\')
            for row in csv_reader:
                arr.append(row)
        return arr