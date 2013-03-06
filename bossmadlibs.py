#!/usr/bin/env python

# madlibs.py v1.0.0
# Madlibs-like game
#
# Changelog:
# v1.0.0 (09/03/2010) - Initial release
#
# Copyright 2010 Benjamin Braithwaite
# Modified by Deb Nicholson 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# imports template strings capability

from string import Template

version = '1.0.0'

# hello to users!

print "Welcome to Madlibs!"
print

# madlib template

madlib100Template = Template('\nHi $nick. I hope you can help me with something. \n'
'As you know, we are trying to build the $super $web for $pro that the world \n'
'has ever seen, and we are planning to localize it for $num new countries this month. \n'
'Everyone is working their $body to the bone around here. \n\n'
'So when you engage in $bad, it makes the other contributors feel $emo \n'
'and that hurts the whole project. \n'
'What do you think we should do about that?\n')

# create and fill dictionary of user's choices

madlib100Choices = {}

madlib100Choices['nick'] = raw_input("Please enter an IRC nick: ")
madlib100Choices['super'] = raw_input("Please enter a superlative: ")
madlib100Choices['web'] = raw_input("Please enter a type of web service: ")
madlib100Choices['pro'] = raw_input("Please enter a profession: ")
madlib100Choices['num'] = raw_input("Please enter a number: ")
madlib100Choices['body'] = raw_input("Please enter a plural body part: ")
madlib100Choices['bad'] = raw_input("Please enter a bad project behavior: ")
madlib100Choices['emo'] = raw_input("Please enter a negative emotion: ")


# insert user's choices into madlib template & print

print madlib100Template.substitute(madlib100Choices)

raw_input ('Press <enter> to exit.')
