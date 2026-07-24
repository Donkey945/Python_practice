import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')
a = vowel_pattern.findall('RoboCop eats BABY FOOD.')
print(a)
