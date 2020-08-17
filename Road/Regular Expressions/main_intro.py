#       Regular Expression (Regex)

    #   \d  -   any decimal digit
    #   \D  -   any non-decimal digit
    #   \s  -   any whitespace char
    #   \S  -   any non-whitespace char
    #   \w  -   any alphanumeric char
    #   \W  -   any non-alphanumeric char

    #   I   -   Ignorecase
    #   L   -   Locale
    #   M   -   Multiline
    #   X   -   Verbose


    #   match()
    #   search()
    #   findall()
    #   fininter()

import re

big_text = "Most letters and characters will simply match themselves . ^ $ * + ? { } [ ] \ | ( ) 456456 45 555599 Lucas" 

rege = re.compile(r'\d')
p = re.compile('[a-z]+')
p.match('')
m = p.match('tempo')

p = re.compile( '\\D' )
m = p.match('string goes here')
#if m:
#    print('Match found')
#else:
#    print('Something is wrong')

p = re.compile(r'\d+')
m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
#print(m)

p = re.compile('(ab)*')
m = p.match('abababababab')

#   Pegando um email em uma string
p = re.compile('[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+')
m = p.match('amado@local.com.br, is the work email')
#print(m)

#   Pegando determinado username em um email

p = re.compile('[^@]+')
m = p.match('amado@local.com.br')
print(m)

