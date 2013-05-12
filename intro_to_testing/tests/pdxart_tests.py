from nose.tools import *
from pdxart import PdxArt

def test_pdxart():
    """ Test loading PdxArt class without arguments """
    art = PdxArt()


def test_header():
    art = PdxArt()
    header = art.header()

    expected_header = [ 'this', 'that' ]
    assert_equal(expected_header, header)


def test_locations():
    """ Test that latitude/longitude are valid """
    art = PdxArt()
    for location in art.locations():
        yield check_location, location

def check_location(location):
    for x in list(location):
        assert_true(type(x) is str)
        if x != '':
            x_float = float(x)
            assert_true(type(x_float) is float)
