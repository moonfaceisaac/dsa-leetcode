numsx = [1,2,3,4,5,6]
print (len(numsx))


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        nums2 = []
        arrResult = []
        for i in range(n,len(nums)):
            nums2.append(nums[i])
        for y in range(0,len(nums)):
            if len(arrResult) == 0:
                x=0
            else:
                x+=1
            if (x == n):
                break
            else:
                arrResult.append(nums[y])
                for j in range (0,len(nums2)):
                    arrResult.append(nums2[j+x])
                    break

        return arrResult  


resultSolution = Solution()
print(resultSolution.shuffle(numsx,3))