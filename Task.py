n=int(input("enter list length:"))
for i in range(n):
    a=int(input("enter a number:"))
    lis.append(a)
print(lis)
while True:
    options=["Options","1.insert a new value","2.delete a new value","3.sort the list","4.reverse the list","5.exit the program"]
    for i in options:
        print(i)
    one=int(input("enter a option to execute:"))
    if one==1:
        bc=int(input("enter a value to insert:"))
        lis.append(bc)
        print("New list=",lis)
    elif one==2:
        ac=int(input("enter a value to delete:"))
        if ac in lis:
            lis.remove(ac)
            print("New list=",lis)
        else:
            print("not a vaid number")
    elif one==3:
        lis.sort()
        print("New  sorted list=",lis)
    elif one==4:
        lis.reverse()
        print("Reversed list=",lis)
    elif one==5:
        print("exiting the program")
        break 
    else:
        print("not in option")