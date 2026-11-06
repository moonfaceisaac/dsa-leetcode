# stringList = ['G','G','A','A','T','T','T','T']



# def counterString(stringListx):

#     counterT = 0
#     counterC = 0
#     counterG = 0
#     compareList = []
#     LAST_NUM_G = None
#     LAST_NUM_T = None
#     LAST_NUM_C = None
#     for i in stringListx:
#         if (i == "G"):
#             if (LAST_NUM_G != "G"):
#                 counterG = 0
#                 counterG += 1
#                 LAST_NUM_G = i
#             else:
#                 counterG += 1
#                 LAST_NUM_G = i
#         else:
#             pass
#             LAST_NUM_G = i
#         compareList.append(counterG)
#     for i in stringListx:
#         if (i == "T"):
#             if (LAST_NUM_T != "T"):
#                 counterT = 0
#                 counterT += 1
#                 LAST_NUM_T = i
#             else:
#                 counterT += 1
#                 LAST_NUM_T = i
#         else:
#             pass
#             LAST_NUM_T = i
#         compareList.append(counterT)
#     for i in stringListx:
#         if (i == "C"):
#             if (LAST_NUM_C != "C"):
#                 counterC = 0
#                 counterC += 1
#                 LAST_NUM_C = i
#             else:
#                 counterC += 1
#                 LAST_NUM_C = i
#         else:
#             pass
#             LAST_NUM_C = i
#         compareList.append(counterC)

#     return (print(max(compareList)))

# counterString(stringList)

        

stringList = ['G','G','A','A','T','T','T','T','T''G','G','T','T']



def counterString(stringListx):

    counterT = 0
    counterC = 0
    counterG = 0
    compareList = []
    LAST_NUM = None
    for i in stringListx:
        if (i == "G"):
            if (LAST_NUM != "G"):
                compareList.append(counterG)
                counterG = 0
                counterG += 1
                LAST_NUM = i
            else:
                counterG += 1
                LAST_NUM = i
        elif (i == "T"):
            if (LAST_NUM != "T"):
                compareList.append(counterT)
                counterT = 0
                counterT += 1
                LAST_NUM = i
            else:
                counterT += 1
                LAST_NUM = i
        elif (i == "C"):
            if (LAST_NUM != "C"):
                compareList.append(counterC)
                counterC = 0
                counterC += 1
                LAST_NUM = i
            else:
                counterC += 1
                LAST_NUM = i
        else:
            pass
            LAST_NUM = i

    return (print(max(compareList)))

counterString(stringList)

        
