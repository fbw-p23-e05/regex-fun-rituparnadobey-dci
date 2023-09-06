# 7. Write a Python program to find sequences of lowercase letters joined by an underscore.



import re

pattern = '[a-z]\_'

match1= (re.search(pattern, 'abcd_'))
match2= (re.search(pattern, 'cder_'))
match3= (re.search(pattern, 'gfrs_jki'))
match4= (re.search(pattern, 'vgtf_'))
match5= (re.search(pattern, '_fgtr'))

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