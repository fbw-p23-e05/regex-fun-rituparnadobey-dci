# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


import re

pattern = '[a-zA-Z][0-9]'

match = (re.search(pattern, 'Pattern123'))

if match:
    print('Result matching:',match.group())
else:
    print('Result not matching')


