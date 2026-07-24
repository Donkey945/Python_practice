import re
at_re = re.compile(r'.at')
a = at_re.findall("The cat in the hat sat at the flat mat.")
print(a)