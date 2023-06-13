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

gl_dict_01_en = None
gl_dict_01_ru = None
gl_dict_02_en = None
gl_dict_02_ru = None
gl_dict_03 = None

##########################################################

def create_dict_01_en():

    global gl_dict_01_en

    if not gl_dict_01_en:
        gl_dict_01_en = localizedict.localizedict( "resources/locations", Language.en )

    return gl_dict_01_en

##########################################################

def create_dict_01_ru():

    global gl_dict_01_ru

    if not gl_dict_01_ru:
        gl_dict_01_ru = localizedict.localizedict( "resources/locations", Language.ru )

    return gl_dict_01_ru

##########################################################

def create_dict_02_en():

    global gl_dict_02_en

    if not gl_dict_02_en:
        gl_dict_02_en = localizedict.localizedict( "resources/specializations", Language.en )

    return gl_dict_02_en

##########################################################

def create_dict_03():

    global gl_dict_03

    if not gl_dict_03:
        gl_dict_03 = localizedict.localizedict( "resources/specializations", Language.en, True )

    return gl_dict_03

##########################################################

def create_dict_02_ru():

    global gl_dict_02_ru

    if not gl_dict_02_ru:
        gl_dict_02_ru = localizedict.localizedict( "resources/specializations", Language.ru )

    return gl_dict_02_ru

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

def test_05():

    d = create_dict_02_en()

    idd = 10000

    word = d.get( idd )

    print( f"test_05: id '{idd}', word = {word}" )

##########################################################

def test_06():

    d = create_dict_03()

    idd = 10000

    try:
        word = d.get( idd )

        print( f"test_06: id '{idd}', word = {word}" )

    except e as Exception:

        print( f"test_06: id '{idd}', got exception {e}" )

##########################################################

def test():

    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
