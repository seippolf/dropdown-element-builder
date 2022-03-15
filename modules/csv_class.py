import csv

class CSV:
    '''
        A class representing a CSV file for ease of use
        and code readability

        ...

        Attributes
        ----------
        _arr : list
            internal list
        _index : str
            internal index for iteration
        
        Methods
        -------
        _build_arr(file):
            Builds internal array around passed file
    '''
    def __init__(self, file):
        '''
            Constructs a CSV object from given file

            Parameters
            ----------
            file : str
                string pointing to CSV file
        '''
        self._arr = self._build_arr(file)
        self._index = 0
    
    def __len__(self):
        return len(self._arr)
    
    def __getitem__(self, index):
        return self._arr[index]
    
    def __iter__(self):
        return self

    def __next__(self):
        i = self._index
        self._index += 1
        if self._index > len(self._arr):
            # Set index back to 0 and stop
            self._index = 0
            raise StopIteration
        return self._arr[i]    

    def _build_arr(self, file):
        '''
            Build internal list from file passed to constructor
        '''
        arr = []
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, escapechar='\\')
            for row in csv_reader:
                arr.append(row)
        csv_file.close()
        return arr