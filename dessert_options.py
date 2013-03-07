#!/usr/bin/env python

# Find out good places to get dessert from pyladies
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

# imports template strings capability

from string import Template

version = '0.1'

# hello to users!

print "Welcome to the Portland PyLadies Dessert Suggester!"
print

dessert_suggestions = {
'Thursday':   "Where do we get alcoholic milkshakes? Lyzi says salt and straw - drinking vinegar",
'Monica': "Sugar cube outside of Lardo, but WTF might be closing",
'Belinda': "Loretta Jean's pies - tiny outlet in cafe velo, east side on division, lemon mererngue",
'Kelly':  "Loves 50/50 - ICE CREAM, salted carmel",
'Jules':  "Rimsky Korsacoffeehouse - Belmont and 11th",
'Portia': "Rimsky Korsacoffeehouse",
'Flora':  "FLORA'S HOUSE, if you show up you will get baked goodies",
'Tracy':  "Helen Bernhard's bakery - YUM 17th and NE Broadway",
'Lyzi':   "Random Order - best pies",
'Selena': "PieKu at backspace",
}

name = raw_input("Please enter the name of a PyLadies member: ")

proper_name = name.title()
if proper_name in dessert_suggestions:
    print proper_name + " says: ",
    print dessert_suggestions[proper_name]
else:
    print "That PyLadies member hasn't left a suggestion yet!"

raw_input ('Press <enter> to exit.')
