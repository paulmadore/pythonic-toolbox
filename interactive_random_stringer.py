#!/usr/bin/python2
# -*- coding: UTF-8 -*-
'''
A simple script that will generate any number of strings of any length, randomly, in an OS-specific manner. The Python random library utilizes local randomness sources, so results may vary. On Linux this script allows the user to easily output said strings either to terminal or to file.

To run, do:
        
        python interactive_rand*

Copyright (c) 2016 P. H. Madore [http://phm.link]


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

import random
import string

limit = int(0)
number_of_strings = raw_input('Number of strings? ')
random_string_length = raw_input('Length of strings: (no limit) ')
print_to_file = raw_input('Print to file? (y/n) ')
print_line_number = raw_input('Print string number? (y/n)')
length = int(random_string_length)

if print_to_file == 'y':
    chop = "".join( [random.choice(string.digits) for i in xrange(length)] )
    file_to_print = raw_input('File name? ')
    with open(file_to_print, 'w+') as file:
        while limit < int(number_of_strings):
            limit+=1
            file.write('String #' + str(limit) + ':')
            file.write(chop + '\n')
            if limit >= number_of_strings:
                file.close()
else:
    while limit < int(number_of_strings):
        choppo = "".join( [random.choice(string.digits) for i in xrange(length)] )
        limit+=1
        if print_line_number == 'n':
            print(choppo)            
        else:
            print('String #' + str(limit) + ':')
            print(choppo)
        
        
        

    
    