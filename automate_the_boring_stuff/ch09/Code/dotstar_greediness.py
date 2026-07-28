import re
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner>')
a = match1.group()

greedy_pattern = re.compile(r'<.*>')
match2 = greedy_pattern.search('<To serve man> for dinner>')
b = match2.group()
print(a,b, sep='\n')