# [Platform] - [Section] - [Lab/Topic name]
  [ATBS] - [CH09] - [regex_revision]
Date: 2026/08/04
Status: finshed

## Where I got stuck / mistakes
1. What is 'raw string'?

2. Should findall() return tuples only?

3. Should  regex '.*?' match 0 each time? 

## Fix
1. a raw string is a string literalprefixed with r. The prefix stops python treating backslashes as escapes, so regex patterns like r'\d\d\d' pass through untouched instead of needing '\\d\\d\\d'.

2. findall() returns a list of strings when there are no groups or just one group, returns a list of tuples only when there are two or more groups.

3. .*? consumes as few characters as possible while still letting the rest of the pattern match. It will return zero if that works, more only when forced.