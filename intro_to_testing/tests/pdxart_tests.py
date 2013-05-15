from nose.tools import *
from pdxart import PdxArt
import unittest

def test_pdxart():
    """ Test loading PdxArt class without arguments """
    art = PdxArt()

@unittest.skip("skipping header test")
def test_header():
    art = PdxArt()
    header = art.header()

    expected_header = [ 'this', 'that' ]
    assert_equal(expected_header, header)


@unittest.skip("skipping location test")
def test_locations():
    """ Test that latitude/longitude are valid """
    art = PdxArt()
    for location in art.locations():
        yield check_location, location

# Generator that doesn't get run because 'test' is not in the function name
def check_location(location):
    for x in list(location):
        assert_true(type(x) is str)
        if x != '':
            x_float = float(x)
            assert_true(type(x_float) is float)
