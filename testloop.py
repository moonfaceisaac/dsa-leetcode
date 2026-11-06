firstArr = [0,1,2,3,10,4,8]

for ind,it in enumerate(firstArr):
    ind+=1
    if ind == len(firstArr):
        print(it)
        break
    else:
        print(it,firstArr[ind])