Public Art in Portland
======================

This is a script to look at data from: http://www.civicapps.org/datasets/public-art

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

Have a look at `tests/some_class_test.py`, which has one test defined, and several other tests marked as "skipped".
