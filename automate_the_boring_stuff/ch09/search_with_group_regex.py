import re
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = pattern.search('My phone number is (415) 555-4242.')
a = mo.group(1)
b = mo.group(2)
print(a,b)
