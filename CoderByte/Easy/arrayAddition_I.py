"""
ARRAY ADDITION I

Have the function ArrayAdditionI(A) take the array of numbers stored in A
and return the string true if any combination of numbers in the array (excluding
the largest number) can be added up to equal the largest number in the array,
otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3]
the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be
empty, will not contain all the same elements, and may contain negative numbers.
"""

ArrayAdditionI = lambda a: a.pop(a.index(max(a))) in list(sum(n for n,k in zip(a,('0'*(len(a) - len('{0:b}'.format(i))) + '{0:b}'.format(i))) if k == '1') for i in range(2**len(a)))