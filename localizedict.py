#!/usr/bin/python3

'''
localizedict.

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

from languages.python.languages import Language
import csv

##########################################################

class localizedict:

    dictt: dict = None
    throw_on_error: bool = None

    def __init__( self, prefix: str, lang: Language, throw_on_error: bool = False ):
        filename = localizedict._generate_filename( prefix, lang )
        self._load( filename )
        self.throw_on_error = throw_on_error

    def __str__(self):
        return str( self.dictt )

    def __len__( self ):
        return len( self.dictt )

    def get( self, idd: int ):

        if self.throw_on_error or ( idd in self.dictt ):
            return self.dictt[ idd ]

        return str( idd )

    ##########################################################

    def _generate_filename( prefix: str, lang: Language ) -> str:
        res = f"{prefix}.{lang.name}.csv"
        return res

    def _load_elem_v_1( data: list, filename: str ) -> []:

        if len( data ) < 2:
            raise Exception( f"load_elem_v_1: broken record in {filename}: expected 2 or more fields, {len(data)} is given" )

        key                 = int( data[0] )
        val                 = data[1]

        return key, val

    def _load_v_1( csvfile, filename: str ) -> dict:

        res = dict()

        reader = csv.reader( csvfile, delimiter=';' )

        for row in reader:

            key, val = localizedict._load_elem_v_1( row, filename )
            res[ key ] = val
            #print( f"DEBUG: _load_v_1: key {key}, val {val}" )

        print( "INFO: _load_v_1: read {} records from {} (v1)".format( len( res ), filename ) )

        return res

    def _load( self, filename: str ):

        with open( filename ) as csvfile:
            self.dictt = localizedict._load_v_1( csvfile, filename )

        print( f"INFO: _load: read {len(self.dictt)} records from {filename}" )

##########################################################
