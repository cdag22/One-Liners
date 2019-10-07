"""
ADDITIVE PERSISTENCE

Have the function AdditivePersistence(n) take the num parameter being passed which
will always be a positive integer and return its additive persistence which is the
number of times you must add the digits in num until you reach a single digit. For example:
if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.
"""

AdditivePersistence = lambda n, i = 0: i if len(str(n)) == 1 else AdditivePersistence(sum(int(d) for d in str(n)), i + 1)