class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        output = []
        iteration = 0
        LAST_NUM = None
        x = sorted(nums, reverse=False)
        print(f"after sorted : {x}")
        for i in x:
            iteration += 1
            if (i in output):
                output.remove(i)
                print(f"Removed Identified Missing : {i}")
            else:
                pass
            if (LAST_NUM in output):
                output.remove(LAST_NUM)
                print(f"Removed Identified Missing : {LAST_NUM}")
            else:
                pass
            if (i != iteration):
                output.append(iteration)
                print(f"Identified Missing : {iteration}")
            else:
                pass
            LAST_NUM = i
            print(LAST_NUM)
            

        return (output)

keyAccess = Solution()
numsx = [10,2,5,10,9,1,1,4,3,7]
# numsx = [6,6,6,6,6,6]
print(keyAccess.findDisappearedNumbers(numsx))
            