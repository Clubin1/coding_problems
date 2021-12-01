class Algorithim(object):
    # SlidingWindow Algorithim
    # Good at subset/subarray problems for O(n)     
    def slidingWindow(self, list, n):
        # handle test case if arr is empty, return -1
        if len(list) < n: 
            return -1
        
        # establish baseline of max sum
        max_sum = 0
        for i in range(n):
            max_sum += list[i]
        
        # set pointers, and temp sum
        i = 0
        j = n
        temp_sum = max_sum

        # while leading pointer is less than len of list
        # temp = temp 
        while(j < len(list)): 
            temp_sum = temp_sum - list[i] + list[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
            i+=1
            j+=1

        return max_sum


    print(slidingWindow(object, [1,4,6,1], 2))
