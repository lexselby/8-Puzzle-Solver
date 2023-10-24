import json


class parser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        file = open(self.filename)  # opening the input file
        puzzle = json.load(file)  # loading the data from the input file
        return puzzle  # returning the extracted puzzle data

