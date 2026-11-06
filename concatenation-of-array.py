class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ansArray = nums.copy()
        for i in nums:
            ansArray.append(i)

        return (ansArray)

listA = [1,2,3]
accessSolution = Solution()

print(accessSolution.getConcatenation(listA))

