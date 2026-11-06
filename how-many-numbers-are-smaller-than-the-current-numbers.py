# input : nums - i = [12384]

# output  : [0,1,2,4,3] - each item represents how many fellow smaller numbers on the list the item has 

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        second_iteration = 0
        counter = 0
        output = []
        for i in nums:
            counter = 0
            for j in nums:
                second_iteration += 1
                if (j<i): 
                    counter += 1
                else:
                    pass
                if second_iteration == len(nums):
                    output.append(counter)
                    second_iteration = 0
                    break
                else:
                    pass
        return (output)
                    
                



numsx = [2,3,6,1]
keyAccess = Solution()
print(keyAccess.smallerNumbersThanCurrent(numsx))

# edge cases:
# [0,0]
