import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
a = pattern.findall('Cell: 425-555-9999 Work: 212-555-0000')
print(a)

new_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
b = new_pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(b)

newer_pattern = re.compile(r'(\d{3})')
a = newer_pattern.findall('1234')
b = newer_pattern.findall('12345')
c = newer_pattern.findall('123456')
print(a,b,c)