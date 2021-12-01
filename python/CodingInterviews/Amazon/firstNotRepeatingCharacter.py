class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # map = {}
        
        # for i in range(len(s)):
        #     currChar = s[i]
        #     if currChar in map:
        #         map[currChar] = map.get(currChar) + 1
        #     else:
        #         map[currChar] = 1

        # for x in range(len(s)):
        #     currChar = s[x]
        #     if map[currChar] == 1:
        #         return currChar
        # else:
        #     return -1

        map = {}

        for i in range(len(s)):
            currChar = s[i]
            if currChar in map:
                map[currChar] = map.get(currChar) + 1
            else:
                map[currChar] = 1

        for i in range(len(s)):
            currChar = s[i]
            if map[currChar] == 1:
                return currChar
        return -1
    
    print(firstUniqChar(object, "aabbmcvvvc"))
