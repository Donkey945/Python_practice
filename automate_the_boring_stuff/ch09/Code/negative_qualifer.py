import re
consonant_pattern = re.compile(r'[^aeiouAEIOU]')
a = consonant_pattern.findall('RoboCop eats BABY FOOD.')
print(a)
