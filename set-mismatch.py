class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicated = None
        replaced = []
        LAST_NUM = None
        output = []
        normal_count = []
        # iteration = 0
        x = sorted(nums, reverse=False)
        for i in range(1,len(x)+1,1):
            normal_count.append(i)
        for i,j in zip(x,normal_count):
            # iteration += 1
            # FOR CHECKING REPLACED
            if (j not in x):
                if (len(replaced) > 0):
                    pass
                    print("passed1")
                else:
                    replaced.append(j)
                    print("passed2")
            else:
                pass
            # FOR CHECKING DUPLICATED
            if (LAST_NUM == i):
                duplicated = i
            else:
                pass
            LAST_NUM = i
            
        output.append(duplicated)
        output.append(replaced[0])
        
        return (output)
    


input = [1,5,3,2,2,7,6,4,8,9]

keyAccess = Solution()
print(keyAccess.findErrorNums(input))

