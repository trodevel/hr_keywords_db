#!/usr/bin/python3

'''
localizedict test.

Copyright (C) 2023 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

from hr_keywords.python.languages import Language

import localizedict

##########################################################

gl_dict_01 = None
gl_dict_02 = None
gl_dict_03 = None
gl_dict_04 = None
gl_dict_05 = None

##########################################################

def create_dict_01_en():

    global gl_dict_01

    if not gl_dict_01:
        gl_dict_01 = localizedict.localizedict( "resources/locations", Language.en )

    return gl_dict_01

##########################################################

def create_dict_01_ru():

    global gl_dict_02

    if not gl_dict_02:
        gl_dict_02 = localizedict.localizedict( "resources/locations", Language.ru )

    return gl_dict_02

##########################################################

def create_dict_02_en():

    global gl_dict_03

    if not gl_dict_03:
        gl_dict_02 = localizedict.localizedict( "resources/specialization", Language.en )

    return gl_dict_03

##########################################################

def create_dict_02_ru():

    global gl_dict_04

    if not gl_dict_04:
        gl_dict_04 = localizedict.localizedict( "resources/specialization", Language.ru )

    return gl_dict_04

##########################################################

def test_01():

    d = create_dict_01_en()

    idd = 2867714

    word = d.get( idd )

    print( f"test_01: id '{idd}', word = {word}" )

##########################################################

def test_02():

    d = create_dict_01_ru()

    idd = 2867714

    word = d.get( idd )

    print( f"test_02: id '{idd}', word = {word}" )

##########################################################

def test_03():

    d = create_dict_02_en()

    idd = 121

    word = d.get( idd )

    print( f"test_03: id '{idd}', word = {word}" )

##########################################################

def test_04():

    d = create_dict_02_ru()

    idd = 121

    word = d.get( idd )

    print( f"test_04: id '{idd}', word = {word}" )

##########################################################

##########################################################

def test():

    test_01()
    test_02()
    test_03()
    test_04()
#    test_05()
#    test_06()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
