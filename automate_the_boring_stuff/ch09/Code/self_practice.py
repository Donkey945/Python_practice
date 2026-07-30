import re
pattern = re.compile(r'a{1,3}?')
match = pattern.search("aaapple")
a = match.group()
print(a)