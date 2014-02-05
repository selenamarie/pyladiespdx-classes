Prep for class
--------------

There are a few things you can do before class if you want to get a head start. You don't have to do any of this to participate, and you'll be working in pairs.

If you have never been to a PyLadies meetup before:

Totally not a problem! There are a few things you'll need on your laptop to play along:

    Python http://python.org/download/
    easy_install: http://pypi.python.org/pypi/setuptools
    git: https://help.github.com/articles/set-up-git

If you have any trouble getting Python or easy_install on your computer, just let us know when you arrive.

If you have been to a PyLadies meetup before, or the above instructions were way too easy for you: 

Glad to have you back and awesome! Please take a few minutes to set up the TwitterAPI app. Open up a terminal (Terminal in Mac OS X, command.exe in Windows)

Clone the TwitterAPI repo:
    git clone https://github.com/pyladiespdx/TwitterAPI.git
or, if you have your SSH key set up:
    git clone git@github.com:pyladiespdx/TwitterAPI.git

And then go through the instructions at:

https://github.com/pyladiespdx/TwitterAPI

Here are the details that you can use for now to put into your 'config.py':

    import twitter
    api = twitter.Api(consumer_key='qhN19WJIpzkEJiFsOccFdA',
        consumer_secret='yfRLLonNu9i1o4sA9rzH6JEKOgNcyaMpq2oynt2A6io',
        access_token_key='305854397-8x1GT2pk6Wakg5LoHBVkY6SuLgKS3dmnsUEtYWAn',
        access_token_secret='M2nGNxD01mYx3ebN04pvK6F0wTbfdmLZjL3e42xE4')

After you read the instructions on github that should make a bit more sense. :) If not, just ask when you get to class.

If ALL OF THAT was easy as pie:

You rock. Now, take a minute and set up your Twitter API credentials:

    Go to: https://dev.twitter.com/ 
    Sign In with your Twitter account (create a Twitter account if you don't have one already) 
    Go to: https://dev.twitter.com/apps 
    Click "Create a new application" and follow the instructions. 

Thanks for reading, and see you tonight!


Post assessment
----------------

Let us know how we did:
https://docs.google.com/forms/d/1kLXNNZ7bJ9_cej9-1exKi8nIDcd66sEgdlDZFHC-mHA/viewform
or if you're typing this in: http://bit.ly/K4QYOz
