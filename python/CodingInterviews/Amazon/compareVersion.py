class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        
        len1 = len(version1_list)
        len2 = len(version2_list)
        
        for i in range(max(len1, len2)):
            i1 = version1_list[i] if i < len1 else 0
            i2 = version2_list[i] if i < len2 else 0
            
            if i1 != i2:
                return 1 if i1 > i2 else -1
            
        return 0

    print(compareVersion(object, "1.1", "1.02"))