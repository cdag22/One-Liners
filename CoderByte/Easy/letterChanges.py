"""
LETTER CHANGES

Have the function LetterChanges(str) take the str parameter being passed
and modify it using the following algorithm. Replace every letter in the
string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
"""

LetterChanges = lambda s: ''.join(chr(ord(c)+1).upper() if (c in 'dhnt') else 'A' if (c == 'z') else chr(ord(c)+1) if c.isalpha() else c for c in s)