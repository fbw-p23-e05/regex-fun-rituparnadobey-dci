# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.


import re

import re

pattern = 'gib?erish'

match1= (re.search(pattern, 'gibberish'))
match2= (re.search(pattern, 'giberish'))
match3= (re.search(pattern, 'gierish'))
match4= (re.search(pattern, 'gieeerish'))
match5= (re.search(pattern, 'gieeorish'))

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
