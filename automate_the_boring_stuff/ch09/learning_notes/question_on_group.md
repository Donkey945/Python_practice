# [Platform] - [Section] - [Lab/Topic name]
  [ATBS] - [Chapter09] - [extracting_info_project]
Date: 2026/08/03
Status: unfinshed

## Where I got stuck / mistakes
1. for an example of regex '(abc)abc' to apply findall() in the text of 'abcabcabcabc', i thought i can specifically print "group 1 only" which requires an extra step to do so.

2. Thought the unparenthesized text in the sample of regex '(abc)abc'(the abc after (abc)) was excluded from the matching.


## Fix
1. However, a pattern with exactly one group already returns just that group, if there are two capturing parentheses in the pattern, findall() will output a tuple with 2 elements: (group1, group2)

2. It is still required for the matching to happen, it's only left out of the output. Capturing controls what's returned, not what must be present.