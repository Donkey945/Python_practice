import re
pattern = re.compile(r'42!?')
a = pattern.search('42!').group()
b = pattern.search('42').group()
print(a, b, sep=', ')

new_pattern = re.compile(r'42?!')
a = new_pattern.search('42!')
b = new_pattern.search('4!')
c = new_pattern.search('42') == None
print(a,b,c, sep='\n')
