Django
======

The goal of this page is to provide a jumping off point for
folks interested in contributing their first patch to an open
source project!

I picked Django because of how friendly their developer community
is, how many open bugs they had that were new-contributor
friendly, and because the devs were very responsive when I asked
for some help.

Two core devs have agreed to review your patches tomorrow,
6/20/2013! :)


Here's how to get started:

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
TAKEN * Redirect logged in user: https://code.djangoproject.com/ticket/12233
* Lacking Documentation on Custom Related Fields Pre-Save Override: https://code.djangoproject.com/ticket/19427
* add login failure events to django.security logger: https://code.djangoproject.com/ticket/20495
TAKEN * https://code.djangoproject.com/ticket/3111 -- as_tr()/as_li() methods for fields
TAKEN * https://code.djangoproject.com/ticket/19560 -- more helpful error when dangerously mixing naive and tz-aware datetimes
* https://code.djangoproject.com/ticket/19830 -- use the admin's login form for the staff_required decorator
* https://code.djangoproject.com/ticket/20218 -- object-level permission checking in default backend
* https://code.djangoproject.com/ticket/18355 -- an OrderingViewMixin



