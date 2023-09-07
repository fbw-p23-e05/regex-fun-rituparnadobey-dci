# 11. Write a Python program that matches a word at the end of a string, with optional punctuation.


import re

pattern = '\w+[^a-zA-Z0-9]*$'

match1= (re.search(pattern, 'Thereisacat%'))
match2= (re.search(pattern, 'socutecat)'))
match3= (re.search(pattern, 'petercat1234'))
match4= (re.search(pattern, 'cheatercat&'))
match5= (re.search(pattern, 'xdfcat*§$%'))

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