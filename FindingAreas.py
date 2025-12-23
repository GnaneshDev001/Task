while True:
    import math as M
    options=["Find Areas of","1.Square","2.Rectangle","3.Circle","4.Triangle"]
    for i in options:
        print(i)
    num=int(input("Enter a option number to Required Areas:"))
    if num==1:
        side=abs(int(input("enter  side of a square:")))
        print(side*side)
    elif num==2:
        length=abs(int(input("enter length of rectangle:")))
        breadth=abs(int(input("enter breadth of rectangle:")))
        print(length*breadth)
    elif num==3:
        radius=abs(int(input("enter the radius of Circle:")))
        print(M.pi*(radius*radius))
    elif num==4:
        height=abs(int(input("enter the height of Triangle:")))
        breadthh=abs(int(input("enter the breadth of Triangle:")))
        print(height*breadthh/2)
        break
    else:
        print("not valid")