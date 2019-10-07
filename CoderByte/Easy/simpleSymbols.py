"""
SIMPLE SYMBOLS

Have the function SimpleSymbols(str) take the str parameter being passed
and determine if it is an acceptable sequence by either returning the string
true or false. The str parameter will be composed of + and = symbols with several
characters between them (ie. ++d+===+c++==a) and for the string to be true each
letter must be surrounded by a + symbol. So the string to the left would be false.
The string will not be empty and will have at least one letter.
"""

SimpleSymbols = lambda s: sum(1*(k != 0 and k != len(s)-1 and s[k-1]=='+' and s[k+1]=='+') for k in range(len(s)) if s[k].isalpha()) == len(''.join(c for c in s if c.isalpha()))
