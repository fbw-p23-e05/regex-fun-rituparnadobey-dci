# 10. Write a Python program that matches a word at the beginning of a string.

import re

pattern = '^(dog).*'

match1= (re.search(pattern, 'dogocoin'))
match2= (re.search(pattern, 'A_ads'))
match3= (re.search(pattern, 'dogmatic'))
match4= (re.search(pattern, 'godon'))
match5= (re.search(pattern, 'adogs'))

if match1:
    print('Match1 found:',match1.group())
else:
    print('Match not found.')
if match2:
    print('Match2 found:',match2.group())
else:
    print('Match not found.')
if match3:
    print('Match3 found:',match3.group())
else:
    print('Match not found.')
if match4:
    print('Match4 found:',match4.group())
else:
    print('Match not found.')
if match5:
    print('Match5 found:',match5.group())
else:
    print('Match not found.')