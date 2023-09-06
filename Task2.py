# 2. Write a Python program that matches a string that has an a followed by zero or more b's.

import re

pattern = 'swim*ing po*l'

match1= (re.search(pattern, 'swimming pool'))
match2= (re.search(pattern, 'swimmmmming pooool'))
match3= (re.search(pattern, 'swiing pl'))
match4= (re.search(pattern, 'swimaing pül'))

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