# 3. Write a Python program that matches a string that has an a followed by one or more b's.


import re

pattern = 'Bub+le sho+ter'

match1 = (re.search(pattern, 'Bubble shooter'))
match2 = (re.search(pattern, 'Bubbbbble shoooooter'))
match3 = (re.search(pattern, 'Bule shooter'))
match4 = (re.search(pattern, 'Bubble shter'))
match5 = (re.search(pattern, 'Bubblo shootex'))


if match1:
    print('Match1 found:',match1.group())
else:
    print('Match not found')
if match2:
    print('Match2 found:', match2.group())
else:
    print('Match not found')
if match3:
    print('Match3 found:', match3.group())
else:
    print('Match not found')
if match4:
    print('Match4 found:', match4.group())
else:
    print('Match not found')
if match5:
    print('Match5 found:', match5.group())
else:
    print('Match not found')
