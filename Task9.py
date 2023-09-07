# 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.


import re

pattern = '(a.+)b$'

match1= (re.search(pattern, 'a_,.ölb'))
match2= (re.search(pattern, 'A_ads'))
match3= (re.search(pattern, 'a....b'))
match4= (re.search(pattern, 'v99b'))
match5= (re.search(pattern, 'a4587b'))

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