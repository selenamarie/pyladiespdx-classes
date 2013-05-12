#!/usr/bin/env python

import csv
import json as simplejson
import argparse
import re


def main():
    # Meta exercise: Add a configuration file
    conf_parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, add_help=False)
    conf_parser.add_argument("--config", dest="filename", help="Config File input", metavar="FILE", default=None)
    args, remaining_argv = conf_parser.parse_known_args()

    if args.filename:
        config = ConfigParser.SafeConfigParser()
        config.read([args.filename])
        defaults = dict(config.items("Defaults"))
    else:
        defaults = { "option":"default" }

    argparser = argparse.ArgumentParser(parents=[conf_parser])
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
    argparser.set_defaults(**defaults)
    args = argparser.parse_args(remaining_argv)

    pdxart = PdxArt()
    if args.titles:
        pdxart.titles()
    elif args.descriptions:
        pdxart.descriptions()
    elif args.artists:
        pdxart.artists()
    elif args.artists_by_medium:
        pdxart.artists_by_medium(args.artists_by_medium)
    elif args.medium:
        pdxart.medium()
    elif args.medium_type:
        pdxart.medium_by_type(args.medium_type)
    elif args.asjson:
        pdxart.as_json()

class PdxArt(object):

    def __init__(self):
        # Meta exercise: Make opening a file by filename specified on the command-line
        self.csvfile = open('public_art.csv', 'rb')
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
            print t

    def descriptions(self):
        header = self.header
        art = self.art
        # Exercise: Transform description for loop into a list comprehension
        descriptions = []
        for row in art:
            descriptions.append(self.transform_dict(row)['description'])

        for d in descriptions:
            print d

    def artists(self):
        # Exercise: Return only artists
        print "Not implemented"

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
                print work['artist']

    def medium(self):
        header = self.header
        art = self.art
        # EXAMPLE: Return only mediums
        mediums = [ self.transform_dict(row)['medium'] for row in art ]
        # Exercise: sort and only print unique mediums -- hint: See sorted and set
        for m in mediums:
            print m

    def medium_by_type(self, medium_type):
        header = self.header
        art = self.art
        # EXAMPLE: Return mediums of a certain type
        mediums = [ self.transform_dict(row)['medium'] for row in art ]
        regex = re.compile( '(' + medium_type + ')' )
        for m in mediums:
            match = re.search(regex, m)
            if match:
                print m

    def as_json(self):
        header = self.header
        art = self.art
        # EXAMPLE: Return all as JSON
        alljson = [ self.transform_json(row) for row in art ]
        for j in alljson:
            print j

    def locations(self):
        # Exercise: Return only locations
        print "Not implemented"

    def artists_by_firstname(self, name):
        # Exercise: search for artists by first name
        print "not implemented"

    def thumbnail(self):
        # Exercise: download the thumbnails of all the works of art
        print "not implemented"

    def recid(self):
        # Exercise: strip the recid out of the detail_url
        print "not implemented"

    # Meta exercise: Only return unique rows for all functions
    # Meta exercise: Allow values to be returned sorted by date modified (either most recent, or least recent)
    # Meta exercise: Find other interesting attributes of the data and write your own function!
    # Meta exercise: Make calling of functions more efficient than using the "if-then-else" loop

    def transform_dict(self, row):
        header = self.header
        return dict(zip(header, row))

    def transform_json(self, row):
        header = self.header
        transforms = dict(zip(header, row))
        return simplejson.dumps(transforms)

if __name__ == '__main__':
    main()
