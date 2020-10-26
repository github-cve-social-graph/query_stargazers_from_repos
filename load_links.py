import csv

def load_links(fileName):

    with open(fileName) as f:
        reader = csv.reader(f)
        data = list(reader)

    return data[0]


