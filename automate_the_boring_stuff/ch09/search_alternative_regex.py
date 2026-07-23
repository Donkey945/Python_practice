import re
pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
a = match.group()
b = match.group(1)
print(a,b)
