import re
ends_with_number = re.compile(r'\d$')
a = ends_with_number.search('Your number is 42')
b = ends_with_number.search('Your number is forty two.') == None
print(a,b, sep='\n')