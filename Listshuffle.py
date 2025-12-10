#shufflying values by slicing the list and append to the new list pairs
li=[1,2,3,4,5,6]
divide= len(li)//2
print(divide)
player_Ids=li[:divide]
scores=li[divide:]
res_ult=[]
for i in range(divide):
    res_ult.append(player_Ids[i])
    res_ult.append(scores[i])
print(res_ult)