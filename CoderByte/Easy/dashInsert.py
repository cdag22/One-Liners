"""
DASH INSERT

Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
"""

DashInsert = lambda s: ''.join(s[i] + '-' if (int(s[i]) % 2 == 1 and int(s[i+1]) % 2 == 1) else s[i] for i in range(len(s) - 1)) + s[-1]