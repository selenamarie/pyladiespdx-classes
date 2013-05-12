#!/usr/bin/env python

import csv
import json as simplejson
import argparse
import re


def main():
    # Meta exercise: Add a configuration file
    conf_parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter, add_help=False)
    conf_parser.add_argument("--config", dest="filename",
        help="Config File input", metavar="FILE", default=None)
    args, remaining_argv = conf_parser.parse_known_args()

    if args.filename:
        config = ConfigParser.SafeConfigParser()
        config.read([args.filename])
        defaults = dict(config.items("Defaults"))
    else:
        defaults = { "option":"default" }

    argparser = argparse.ArgumentParser(parents=[conf_parser])
    argparser.add_argument("--file", help="Public Art source file",
        action="store", default="public_art.csv")
    argparser.add_argument("--titles", help="print titles of public art",
        action="store_true", default=False)
    argparser.add_argument("--descriptions",
        help="print descriptions of public art", action="store_true",
        default=False)
    argparser.add_argument("--artists", help="print artists",
        action="store_true", default=False)
    argparser.add_argument("--medium", help="print mediums",
        action="store_true", default=False)
    argparser.add_argument("--asjson", help="return file contents at json",
        action="store_true", default=False)
    argparser.add_argument("--medium-type", help="print mediums of type TYPE",
        action="store", default=None)
    argparser.add_argument("--artists-by-medium",
        help="print artists based on medium of type TYPE",
        action="store", default=None)
    argparser.add_argument("--locations", help="print locations",
        action="store_true", default=False)
    argparser.set_defaults(**defaults)
    args = argparser.parse_args(remaining_argv)

    pdxart = PdxArt(args.file)

    result = []
    if args.titles:
        result = pdxart.titles()
    elif args.descriptions:
        result = pdxart.descriptions()
    elif args.artists:
        result = pdxart.artists()
    elif args.artists_by_medium:
        result = pdxart.artists_by_medium(args.artists_by_medium)
    elif args.medium:
        result = pdxart.medium()
    elif args.medium_type:
        result = pdxart.medium_by_type(args.medium_type)
    elif args.asjson:
        result = pdxart.as_json()
    elif args.locations:
        result = pdxart.locations()

    for r in result:
        print r

class PdxArt(object):

    def __init__(self, filename='public_art.csv'):
        # Meta exercise: Make opening a file by filename specified on the command-line
        self.csvfile = open(filename, 'rb')
        self.art = csv.reader(self.csvfile, delimiter=',', quotechar='"')
        self.header = self.art.next()

    def __del__(self):
        self.csvfile.close()

    def titles(self):
        header = self.header
        art = self.art
        # EXAMPLE: Return only titles
        titles = [ self.transform_dict(row)['title'] for row in art]
        for t in titles:
            yield t

    def descriptions(self):
        header = self.header
        art = self.art
        # Exercise: Transform description for loop into a list comprehension
        descriptions = []
        for row in art:
            descriptions.append(self.transform_dict(row)['description'])

        for d in descriptions:
            yield d

    def artists(self):
        # Exercise: Return only artists
        yield "Not implemented"

    def artists_by_medium(self, medium_type):
        header = self.header
        art = self.art
        # EXAMPLE: Return artists by medium type, by regular expression
        all_works = [ self.transform_dict(row) for row in art ]
        regex = re.compile( '(' + medium_type + ')' )
        # Exercise: Return *unique* artists by medium type
        # Exercise: Transform for loop into a list comprehension
        for work in all_works:
            match = re.search(regex, work['medium'])
            if match:
                yield work['artist']

    def medium(self):
        header = self.header
        art = self.art
        # EXAMPLE: Return only mediums
        mediums = [ self.transform_dict(row)['medium'] for row in art ]
        # Exercise: sort and only print unique mediums -- hint: See sorted and set
        for m in mediums:
            yield m

    def medium_by_type(self, medium_type):
        header = self.header
        art = self.art
        # EXAMPLE: Return mediums of a certain type
        mediums = [ self.transform_dict(row)['medium'] for row in art ]
        regex = re.compile( '(' + medium_type + ')' )
        for m in mediums:
            match = re.search(regex, m)
            if match:
                yield m

    def as_json(self):
        # EXAMPLE: Return all as JSON
        alljson = [ self.transform_json(row) for row in self.art ]
        for j in alljson:
            yield j

    def locations(self):
        # Return the lat/lng for each piece of art
        locations = [ (self.transform_dict(row)['lat'],
            self.transform_dict(row)['lng'])
            for row in self.art ]
        for location in locations:
            yield location

    def artists_by_firstname(self, name):
        # Exercise: search for artists by first name
        yield "not implemented"

    def thumbnail(self):
        # Exercise: download the thumbnails of all the works of art
        yield "not implemented"

    def recid(self):
        # Exercise: strip the recid out of the detail_url
        yield "not implemented"

    def transform_dict(self, row):
        header = self.header
        return dict(zip(header, row))

    def transform_json(self, row):
        header = self.header
        transforms = dict(zip(header, row))
        return simplejson.dumps(transforms)

if __name__ == '__main__':
    main()
