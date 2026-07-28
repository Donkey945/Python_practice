import re
name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
a = name_match.group(1)
b = name_match.group(2)
print(a,b, sep='\n')