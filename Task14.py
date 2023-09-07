# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

pattern = '[a-zA-Z0-9_]+'

# \w+

match1= (re.search(pattern, 'zeBra_'))
match2= (re.search(pattern, 'zooLogy2_'))
match3= (re.search(pattern, 'LogiC_5'))
match4= (re.search(pattern, '4Zebra_'))
match5= (re.search(pattern, 'zooloGy&'))

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