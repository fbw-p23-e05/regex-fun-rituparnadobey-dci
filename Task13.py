# 13. Write a Python program that matches a word containing 'z', not the start or end of the word.



import re

pattern = '[^z].*[^z]'

# or [a-zA-Y]+z[a-yA-Y]+

match1= (re.search(pattern, 'zebraz'))
match2= (re.search(pattern, 'zoologyz'))
match3= (re.search(pattern, 'zoology'))
match4= (re.search(pattern, 'Zebraz'))
match5= (re.search(pattern, 'zooloGyz'))

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