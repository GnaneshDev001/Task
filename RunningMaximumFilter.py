N=[1,2,1,3,3,4,5,6,1,4,7,1]
Result=[]
Max=0
for x in N:
    if x>=Max:
        Result.append(x)
        Max=x
print(Result)