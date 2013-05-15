from nose.tools import *
from nose.plugins.skip import SkipTest
from example import SampleClass

def test_sample_class():
    """ Verify we get what we expect back from a sample class """
    expected_list = [ 'one', 'two', 'three', 'four', 'five' ]
    s = SampleClass()
    test_list = s.mylist()
    assert_equal(test_list, expected_list)

def test_myname():
    """ Verify that we return myname """
    raise SkipTest
    pass

def test_add_myname_to_mylist():
    """ Verify that we can add myname to mylist """
    raise SkipTest
    pass

def test_add_to_mylist():
    """ Verify that we can add a new element to the list """
    raise SkipTest
    pass
