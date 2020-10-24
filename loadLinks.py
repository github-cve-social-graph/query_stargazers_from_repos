import csv

def loadLinks(fileName):

    with open(fileName) as f:
        reader = csv.reader(f)
        data = list(reader)

    return data[0]


