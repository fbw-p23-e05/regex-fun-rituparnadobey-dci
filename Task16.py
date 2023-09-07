# 16. Write a Python program to remove leading zeros from an IP address.


import re

ip = '024.055.001.080'

output = re.sub('0*(\d*)',r'\1', ip)

print(output)