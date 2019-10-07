"""
LETTER CAPITALIZE

Have the function LetterCapitalize(str) take the str parameter being passed
and capitalize the first letter of each word. Words will be separated by only one space.
"""

LetterCapitalize = lambda s: ' '.join(word[0].upper() + word[1:] for word in s.split())