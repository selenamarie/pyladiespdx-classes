
import csv
import json as simplejson


def transform_json(header, row):
    transforms = dict(zip(header, row))
    return simplejson.dumps(transforms)

with open('public_art.csv', 'rb') as csvfile:
    arte = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = arte.next()

    print ",".join(header)
    alljson = [ transform_json(header, row) for row in arte ]
    for j in alljson:
        print j
