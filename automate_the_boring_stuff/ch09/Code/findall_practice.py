import re
pattern = re.compile(r'(abc)abc(efg)efg')
match = pattern.findall('abcabcabcabcefgefgefgefg')
print(match)

pattern1 = re.compile(r'(abc)abc(efg)efg')
match1 = pattern1.findall('abcabcefgefg')
print(match1)

import re
pattern = re.compile(r'(abc)abc(efg)efg')
match = pattern.findall('abcabcabcabcefgefgefgefg')
print(match)

pattern2 = re.compile(r'(abc)abc(efg)efg')
match2 = pattern2.findall('abcabcefgefgabcabcefgefg')
print(match2)