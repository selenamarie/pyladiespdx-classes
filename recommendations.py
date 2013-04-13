#!/usr/bin/env python

# Pyladies Recommendations
# More general recommendations tool
#
# Changelog:
# v1.0.0 (09/03/2010) - Initial release
#
# Copyright 2013 Selena Deckelmann
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

from string import Template

import json

version = '0.1'

# Pull in the raw data from a file into a string
raw_data = open('cookies.json')
data_string = raw_data.read()
raw_data.close()

# Transform the string into a Python dict using the json module
data_dictionary = json.loads(data_string)

# Say hello to users!
print "Welcome to the Portland PyLadies %s Suggester!" % data_dictionary['type']
print

recommendations = data_dictionary['recommendations']

name = raw_input("Please enter the name of a PyLadies member: ")

proper_name = name.title()
if proper_name in recommendations:
    print proper_name + " says: ",
    print recommendations[proper_name]
else:
    print "That PyLadies member hasn't left a suggestion yet!"

raw_input ('Press <enter> to exit.')

