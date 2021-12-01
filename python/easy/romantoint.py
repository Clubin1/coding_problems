class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    
    table = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    total = 0
    str_len = len(s)
    i = str_len - 1

    while i >= 0:
        if i < str_len - 1 and table[s[i+1]] > table[s[i]]:
            total -+ table[s[i]]
        else:
            total += table[s[i]]
        return total



    print(romanToInt(object, "IV"))