Intro to testing
================

Testing is about verifying functionality:

* Does this function return a list of strings?
* Does this object create an object properly?
* Can this object talk to a database?
* Can these two objects talk to each other?
* Can a system run properly when all the parts are put together?

Unit testing - test each component individually
Integration testing - test interfaces between components
System testing - test a complete system to verify it meets requirements

Python has a built-in class for testing: unittest

There's also another library and executable called nose. Nose is often also
used with Django.

We're going to use Nose.


Setup
=========

Run these commands to get started:

    $ mkdir -p ~/venv ; virtualenv ~/venv/pdxart
    New python executable in /home/selena/venv/pdxart/bin/python
    Installing distribute..............................................................................................................................................................................................done.
    Installing pip...............done.
    $ source ~/venv/pdxart/bin/activate
    $ pip install -r requirements.txt
    $ cat >> ~/.noserc
    [nosetests]
    verbosity=3
    ^D
    $ mkdir -p tests
    $ nosetests

    nose.selector: INFO: /home/selena/repos/pyladies-stuff/projects/intro_to_testing/example.py is executable; skipped
    nose.selector: INFO: /home/selena/repos/pyladies-stuff/projects/intro_to_testing/pdxart.py is executable; skipped

    ----------------------------------------------------------------------
    Ran 0 tests in 0.001s

    OK

Writing your first test
-----------------------

The tool 'nosetests' will look into the directory called 'tests' and try to run
any tests in that directory

To see the current state of our test suite, run `nosetests`.

Have a look at `some_class.py` and see the class that's defined in there.

Have a look at `tests/some_class_test.py`, which has one test defined, and
several other tests marked as "skipped".

See: `https://nose.readthedocs.org/en/latest/testing_tools.html`

Methods you can use include:

* `assert_equal(a, b)`
* `assert_not_equal(a, b)`
* `assert_true(a, b)`
* `assert_false(a, b)`
* `assert_is(a, b) # 2.7`
* `assert_is_not(a, b) # 2.7`
* `assert_is_none(x) # 2.7`
* `assert_is_not_none(x) # 2.7`
* `assert_is_not_none(x) # 2.7`
* `assert_is_in(a, b) # 2.7`
* `assert_is_not_in(a, b) # 2.7`
* `assert_is_instance(a, b) # 2.7`
* `assert_is_not)instance(a, b) # 2.7`


We'll also use SkipTest (from `nose.modules.skip`).

When code is hard to test
=========================

Sometimes it isn't clear how to test a piece of code, or testing it seems like
a lot of work for not a lot of gain.

For example:

    def artists_by_medium(self, medium_type):

How do we test this, when `medium_type` is a regular expression?

Some options:

* Test several different regular expressions
* Cut and paste the output into a list that we compare against

That seems like a lot of work!

Some questions to think about:

* What happens if the file we import changes?
* How do we test regular expressions? (and aren't they already tested?)
* What is the real purpose of this test?
* Could we break this function apart and test the components more easily?


Writing more complex tests
--------------------------

Have a look at `pdxart.py`, a heavily refactored version of the tool you saw
two weeks ago.

This contains a class, and there is a corresponding set of tests in
`tests/pdxart_tests.py`. See if you can run some of these tests and create
a few new ones of your own.


Public Art in Portland
======================

This is a script to look at data from: http://www.civicapps.org/datasets/public-art

