import re

text = "A dogmatic dog eating hotdog with another dog."



matches = re.sub('\Wdog\W',text)

print(matches)

