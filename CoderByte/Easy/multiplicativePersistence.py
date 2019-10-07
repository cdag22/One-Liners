"""
MULTIPLICATIVE PERSISTENCE

Have the function MultiplicativePersistence(n) take the num parameter being passed which will
always be a positive integer and return its multiplicative persistence which is the number of
times you must multiply the digits in num until you reach a single digit. For example: if num
is 39 then your program should return 3 because 3 * 9 = 27 then 2 * 7 = 14 and finally 1 * 4 = 4
and you stop at 4.
"""
MultiplicativePersistence = lambda n : (lambda f, *a: f(f, *a))(lambda f, a = list(int(x) for x in str(n)), c = len(str(n)), d = 0:  a[0] * f(f,a[1:], c - 1, d + 1 ) if c > 0 else d)