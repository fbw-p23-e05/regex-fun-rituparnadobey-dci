# 12. Write a Python program that matches a word containing 'z'.


import re

pattern = '.*z.*'

match1= (re.search(pattern, 'zebra'))
match2= (re.search(pattern, 'awesome'))
match3= (re.search(pattern, 'pizza'))
match4= (re.search(pattern, 'crazy'))
match5= (re.search(pattern, 'lazy'))

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