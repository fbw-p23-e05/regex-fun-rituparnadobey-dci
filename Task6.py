# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.

import re

pattern = '[a-z]a{1}b{2,3}'

match1= (re.search(pattern, 'yarabbb '))
match2= (re.search(pattern, 'cabbbb'))
match3= (re.search(pattern, 'vabb'))
match4= (re.search(pattern, 'babbb'))
match5= (re.search(pattern, 'gaabbb'))

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