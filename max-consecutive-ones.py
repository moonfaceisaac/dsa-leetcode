class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        COUNTER_1 = 0
        COUNTER_ITERATION = 0
        LAST_NUM = None
        COMP_LIST = []
        OUTPUT = 0
        for i in nums:
            COUNTER_ITERATION += 1
            if (i == 1):
                if (LAST_NUM == 1 or LAST_NUM == None):
                    COUNTER_1 += 1
                    LAST_NUM = 1
                    print(f"COND 1: {COUNTER_1}")
                elif (LAST_NUM == 0):
                    COMP_LIST.append(COUNTER_1)
                    COUNTER_1 = 0
                    COUNTER_1 += 1
                    LAST_NUM = 1
                    print(f"COND 2: {COUNTER_1}")
            else: #IF RESULT 0
                LAST_NUM = 0
            if (COUNTER_1 > 0 and COUNTER_ITERATION == len(numsx)):
                COMP_LIST.append(COUNTER_1)
            else:
                pass

        COMP_LIST.sort()
        try:
            OUTPUT = COMP_LIST[len(COMP_LIST)-1]
        except IndexError:
            print("Index Is Out of RANGE")
        finally:
            return (OUTPUT)


numsx = [0,1,1]

solutionResult = Solution()
print(solutionResult.findMaxConsecutiveOnes(numsx))
        