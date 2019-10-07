"""
AB CHECK

Have the function ABCheck(str) take the str parameter being passed and return
the string true if the characters a and b are separated by exactly 3 places anywhere
in the string at least once (ie. "lane borrowed" would result in true because there
is exactly three characters between a and b). Otherwise return the string false.
"""

ABCheck = lambda s: sum(1 * ( (s[k]=='a' and s[k+4]=='b') or (s[k]=='b' and s[k+4]=='a') ) for k in range(len(s) - 4)) >= 1
