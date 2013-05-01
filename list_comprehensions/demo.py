import csv
import json as simplejson
import argparse
import re


def transform_dict(header, row):
    return dict(zip(header, row))

def transform_json(header, row):
    transforms = dict(zip(header, row))
    return simplejson.dumps(transforms)

def titles(header, arte):
    # Exercise: Return only titles
    titles = [ transform_dict(header, row)['title'] for row in arte]
    for t in titles:
        print t

def descriptions(header, arte):
    # Exercise: Return only descriptions
    descriptions = [ transform_dict(header, row)['description'] for row in arte]
    for d in descriptions:
        print d

def artists(header, arte):
    # Exercise: Return only artists
    print "Not implemented"
    pass

def artists_by_medium(header, arte):
    # Exercise: Return only artists
    print "Not implemented"
    pass


def locations(header, arte):
    # Exercise: Return only locations
    print "Not implemented"
    pass

def medium(header, arte):
    # Exercise: Return only mediums
    mediums = [ transform_dict(header, row)['medium'] for row in arte ]
    # Exercise: sort and only print unique mediums
    # hint: sorted and set
    for m in mediums:
        print m

def medium_by_type(header, arte, medium_type):
    # Exercise: Return mediums of a certain type
    mediums = [ transform_dict(header, row)['medium'] for row in arte ]
    regex = re.compile( '(' + medium_type + ')' )
    for m in mediums:
        match = re.search(regex, m)
        if match:
            print m

def artists_by_firstname(header, arte, name):
    # Exercise: search for artists by first name
    print "not implemented"

def artists_by_firstname(header, arte, name):
    # Exercise: search for artists by first name
    print "not implemented"

def thumbnail(header, arte):
    # Exercise: download the thumbnails of all the works of art
    print "not implemented"

def recid(header, arte):
    # Exercise: strip the recid out of the detail_url
    print "not implemented"

def as_json(header, arte):
    # Exercise: Return all as JSON
    alljson = [ transform_json(header, row) for row in arte ]
    for j in alljson:
        print j

def demo(args):

    with open('public_art.csv', 'rb') as csvfile:
        arte = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = arte.next()

        if args.titles:
            titles(header, arte)
        elif args.descriptions:
            descriptions(header, arte)
        elif args.artists:
            artists(header, arte)
        elif args.medium:
            medium(header, arte)
        elif args.medium_type:
            medium_by_type(header, arte, args.medium_type)
        elif args.asjson:
            as_json(header, arte)

if __name__ == '__main__':

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
    argparser.add_argument("--titles", help="print titles of public art", action="store_true", default=False)
    argparser.add_argument("--descriptions", help="print descriptions of public art", action="store_true", default=False)
    argparser.add_argument("--artists", help="print artists", action="store_true", default=False)
    argparser.add_argument("--medium", help="print mediums", action="store_true", default=False)
    argparser.add_argument("--asjson", help="return file contents at json", action="store_true", default=False)
    argparser.add_argument("--medium-type", help="print mediums of type TYPE", action="store", default=None)
    argparser.set_defaults(**defaults)
    args = argparser.parse_args(remaining_argv)

    demo(args)
