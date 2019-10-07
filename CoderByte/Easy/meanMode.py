"""
MEAN MODE

Have the function MeanMode(A) take the array of numbers stored in A and return 1 if
the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should
return 1 because the mode (3) equals the mean (3)). The array will not be empty, will
only contain positive integers, and will not contain more than one mode.
"""

MeanMode = lambda A: 1  * ( int(sum(A) / len(A)) == max(set(A), key = A.count) )
