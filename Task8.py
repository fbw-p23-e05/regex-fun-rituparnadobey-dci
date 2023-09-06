# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.


import re

pattern = '[A-Z]{1}[a-z]'

match1= (re.search(pattern, 'abcd_'))
match2= (re.search(pattern, 'A_adsg'))
match3= (re.search(pattern, 'Vgshb'))
match4= (re.search(pattern, 'vgtoD'))
match5= (re.search(pattern, 'Dghgsz'))

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