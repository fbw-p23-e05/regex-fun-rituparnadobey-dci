# 15. Write a Python program that starts each string with a specific number.


import re

pattern = '[9].*'

# '^9[a-z]'  or ^7\w*

match1= (re.search(pattern, '9zeb125'))
match2= (re.search(pattern, '5oolog'))
match3= (re.search(pattern, '6ology'))
match4= (re.search(pattern, '9raz$%&'))
match5= (re.search(pattern, '9loGyz'))

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