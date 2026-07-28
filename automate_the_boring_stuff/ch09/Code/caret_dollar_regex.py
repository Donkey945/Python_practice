import re
whole_string_is_num = re.compile(r'^\d+$')
a = whole_string_is_num.search('1234567890')
b = whole_string_is_num.search('1234xyz67890') == None
print(a,b,sep='\n')
