Django
======

Contributing page: http://code.djangoproject.com/
https://docs.djangoproject.com/en/1.5/internals/contributing/


Setup
-----

Get the code: 
```bash
    git clone https://github.com/django/django.git
    cd django/tests
    PYTHONPATH=..:$PYTHONPATH python ./runtests.py --settings=test_sqlite
```


Process
-------

* Choose a ticket
* Attempt to reproduce the bug
* Write a failing test
* Implement the fix
* Make sure tests pass
* Update documentation
* Create a patch
* Attach to ticket

Tickets
-------

Recommended:
* Redirect logged in user: https://code.djangoproject.com/ticket/12233
* Lacking Documentation on Custom Related Fields Pre-Save Override: https://code.djangoproject.com/ticket/19427
* add login failure events to django.security logger: https://code.djangoproject.com/ticket/20495
* https://code.djangoproject.com/ticket/3111 -- as_tr()/as_li() methods for fields
* https://code.djangoproject.com/ticket/19560 -- more helpful error when dangerously mixing naive and tz-aware datetimes
* https://code.djangoproject.com/ticket/19830 -- use the admin's login form for the staff_required decorator
* https://code.djangoproject.com/ticket/20218 -- object-level permission checking in default backend
* https://code.djangoproject.com/ticket/18355 -- an OrderingViewMixin



Flask
=====

Contributing page: http://www.pocoo.org/contributing/

Style Guide: http://www.pocoo.org/internal/styleguide/#styleguide

Get the code:

    git clone git@github.com:mitsuhiko/flask.git

Needs: jinja and werkzeug

virtualenv ~/venv/flask
source ~/venv/flask/bin/activate
pip install jinja2 werkzeug itsdangerous

python setup.py build
python run-tests.py


Werkzeug
========

Get the code:

    git clone https://github.com/mitsuhiko/werkzeug



