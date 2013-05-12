from nose.tools import *
from pdxart import PdxArt

def test_pdxart():
    """ Test loading PdxArt class without arguments """
    art = PdxArt()

def test_locations():
    art = PdxArt()
    generator = art.locations()
