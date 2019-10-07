"""
AB CHECK

Have the function ABCheck(str) take the str parameter being passed and return
the string true if the characters a and b are separated by exactly 3 places anywhere
in the string at least once (ie. "lane borrowed" would result in true because there
is exactly three characters between a and b). Otherwise return the string false.
"""
ABCheck = lambda s: sum(1 * ( (s[k]=='a' and s[k+4]=='b') or (s[k]=='b' and s[k+4]=='a') ) for k in range(len(s) - 4)) >= 1


"""
ADDITIVE PERSISTENCE

Have the function AdditivePersistence(n) take the num parameter being passed which
will always be a positive integer and return its additive persistence which is the
number of times you must add the digits in num until you reach a single digit. For example:
if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.
"""
AdditivePersistence = lambda n, i = 0: i if len(str(n)) == 1 else AdditivePersistence(sum(int(d) for d in str(n)), i + 1)


"""
ARITH GEO

Have the function ArithGeo(arr) take the array of numbers stored in arr and return
the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric"
if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1.
An arithmetic sequence is one where the difference between each of the numbers is consistent,
where as in a geometric sequence, each term after the first is multiplied by some constant
or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
Negative numbers may be entered as parameters, 0 will not be entered, no array will contain
all the same elements, and all arrays will contain at least two elements.
"""
ArithGeo = lambda A: 'Arithmetic' if sum(1 * ((A[i+1] - A[i]) == (A[1] - A[0])) for i in range(1, len(A) - 1)) == len(A) - 2 else 'Geometric' if sum(1 * ((A[i+1] // A[i]) == (A[1] // A[0])) for i in range(1, len(A) - 1)) == len(A) - 2 else -1


"""
CHECK NUMS

Have the function CheckNums(num1,num2) take both parameters being passed and
return the string true if num2 is greater than num1, otherwise return the string
false. If the parameter values are equal to each other then return the string -1.
"""
CheckNums = lambda x, y: -1 if x == y else y > x


"""
DASH INSERT

Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
"""
DashInsert = lambda s: ''.join(s[i] + '-' if (int(s[i]) % 2 == 1 and int(s[i+1]) % 2 == 1) else s[i] for i in range(len(s) - 1)) + s[-1]


"""
LETTER CAPITALIZE

Have the function LetterCapitalize(str) take the str parameter being passed
and capitalize the first letter of each word. Words will be separated by only one space.
"""
LetterCapitalize = lambda s: ' '.join(word[0].upper() + word[1:] for word in s.split())


"""
LETTER CHANGES

Have the function LetterChanges(str) take the str parameter being passed
and modify it using the following algorithm. Replace every letter in the
string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
"""
LetterChanges = lambda s: ''.join(chr(ord(c)+1).upper() if (c in 'dhnt') else 'A' if (c == 'z') else chr(ord(c)+1) if c.isalpha() else c for c in s)


"""
MEAN MODE

Have the function MeanMode(A) take the array of numbers stored in A and return 1 if
the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should
return 1 because the mode (3) equals the mean (3)). The array will not be empty, will
only contain positive integers, and will not contain more than one mode.
"""
MeanMode = lambda A: 1  * ( int(sum(A) / len(A)) == max(set(A), key = A.count) )


"""
PALINDROME

Have the function Palindrome(str) take the str parameter being passed
and return the string true if the parameter is a palindrome, (the string
is the same forward as it is backward) otherwise return the string false.
For example: "racecar" is also "racecar" backwards. Punctuation and numbers
will not be part of the string, but spaces may be.
"""
Palindrome = lambda s: ''.join(s.split()) == ''.join(s.split())[::-1]


"""
REVERSE STRING
"""
FirstReverse = lambda s: s[::-1]


"""
SIMPLE ADDING

Have the function SimpleAdding(num) add up all the numbers from 1 to num.
For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
For the test cases, the parameter num will be any number from 1 to 1000.
"""
SimpleAdding = lambda n: n * (n + 1) // 2


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


"""
TIME CONVERT

Have the function TimeConvert(num) take the num parameter being passed and
return the number of hours and minutes the parameter converts to (ie. if num = 63
then the output should be 1:3). Separate the number of hours and minutes with a colon.
"""
TimeConvert = lambda n: str(n // 60) + ':' + str(n % 60)


"""
VOWEL COUNT

Have the function VowelCount(str) take the str string parameter being
passed and return the number of vowels the string contains (ie. "All cows
eat grass and moo" would return 8). Do not count y as a vowel for this challenge.
"""
VowelCount = lambda s: sum(1 * (c.lower() in 'aeiou') for c in s)