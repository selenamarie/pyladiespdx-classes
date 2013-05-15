from nose.tools import *
from example import SampleClass
import unittest

def test_sample_class():
    """ Verify we get what we expect back from a sample class """
    expected_list = [ 'one', 'two', 'three', 'four', 'five' ]
    s = SampleClass()
    test_list = s.mylist()
    assert_equal(test_list, expected_list)

@unittest.skip("skipping myname test")
def test_myname():
    """ Verify that we return myname """
    pass

@unittest.skip("skipping myname_to_mylist test")
def test_add_myname_to_mylist():
    """ Verify that we can add myname to mylist """
    pass

@unittest.skip("skipping add_to_mylist test")
def test_add_to_mylist():
    """ Verify that we can add a new element to the list """
    pass
