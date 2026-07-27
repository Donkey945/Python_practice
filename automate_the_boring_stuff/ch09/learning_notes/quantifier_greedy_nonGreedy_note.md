```markdown
# [Platform] - [Section] - [Lab/Topic name]
# [ATBS] - [chapter09] - [regex]

Date: 2026-07-27
Status: unfinished

## Core concept
{} is the quantifier, it attaches to the preceding element which can be a single element like '1', a character class like '\d' or a group like '(and spam)', it specifies how many times the preceding element must occur.
for example,
1, r'\d{3}' means match exactly 3 digits(can be of any digits, does not need to be the same digit).
2, r'\d{m,n}' means the digit can have minimum m and maximum n inclusively, by default, the regular expression of python is greedy, so the regex will match maximum n by default.
3, r'\d{,n}' stands for "from 0 up to n times occurence". 
   r'\d{m,}' stands for "m times or more with no upper limit".
4, to make the default expression non-greedy, we can add '?' after the quantifier, for example:
   r'\d{1,2}', is greedy and match as many as it can.
   r'\d{1,2}?', is non-greedy and match as few as possible which is 1, expanding to 2 only if overall match requires it. 

## What I did
write down the exercise code and go through the concepts.

## Where I got stuck / mistakes
1. for r'\d{3}', the matching digit does not have to be the same digit, it can be any digit. 
2. non-greedy method that adds '?' after quantifier is not hard limit that it must take the minimum, for example:
r'\d{1,2}?X' matches X after the digit, when the target text is "42X", the regex will not minimally match '4' but also '2' in order to match 'X' which will output '42X'.
```