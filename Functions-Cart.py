# def append_items_price(User:int,size:int)->list:
#     li = []
#     print(f"_Enter {User} user  items price : ______________________")
#     for _ in range(size):
#         li.append(int(input(f"Enter {_ + 1} Item price : ")))
#     return li

# def make_dis(total:int,dis:int)->float:
#     temp_dis_value = total*(dis/100)
#     return total - temp_dis_value

# def log(li:list)->float:
#     temp_sum = sum(li)
#     if temp_sum >= 5000:
#         final_total = make_dis(total=temp_sum,dis=20)
#     elif temp_sum > 1000:
#         final_total = make_dis(total=temp_sum,dis=15)
#     elif temp_sum > 500:
#         final_total = make_dis(total=temp_sum,dis=5)
#     else:
#         final_total = temp_sum
#     return final_total
    

# #start here
# num_Users = int(input("Enter number of users : "))

# items_size = []
# for i in range(1,num_Users+1):
#     temp = int(input(f"Enter the Cart items Size of User_{i} : "))
#     items_size.append(temp)

# total_users_cart_list = []
# for user,size in enumerate(items_size):
#     temp = append_items_price(User=user+1,size=size)
#     total_users_cart_list.append(temp)

# final_cart_after_discount = []

# for user_cart in total_users_cart_list:
#     temp = log(li=user_cart)
#     final_cart_after_discount.append(temp)

# print("_Total Bill Amount")
# for user,total_price in enumerate(final_cart_after_discount):
#     print(f"{user+1} User total price : {total_price} RS")

# # print(final_cart_after_discount)

# Day-3-----Multi-User Shopping Cart Billing

# def arr():
#    num=int(input("enter the no of customers: "))
#    cart=[]
#    for i in range(1,num+1):
#       customer=[]
#       while (True):
#          items=int(input(f"enter the cart items of {i} customer: "))
#          if items==0:
#             break
#          (customer.append(items))
#       cart.append(customer)
#    totals = []
#    for customer in cart:
#       totals.append(sum(customer))
#     #return
#    def dis(totals,discount):
#       final_lis=[]
#       for total in totals: 
#         if total >= 5000:
#             (final_lis.append(total-(total/100)*discount))
#         elif total > 1000:
#             (final_lis.append(total-(total/100)*discount))
#         elif total > 500:
#             (final_lis.append(total-(total/100)*discount))
#         else:
#             return totals
#         return final_lis
#         return dis(totals,20)
# arr()

n=[[100,400,127],
[450,600],
[127,128,57,600],[0,1,6/900],[2500,2500]
]
output=[]
for i in n:
    total=sum(i)
    if total>0 and total<500:
        output.append(total)
    elif total>500 and total<1000:
        discount=total/100*5
        total_price=total-discount
        output.append(total_price)
    elif total>1000 and total<5000:
        discount1=total/100*15
        total_price=total-discount1
        output.append(total_price)
    elif total>=5000:
        discount2=total/100*20
        total_price=total-discount2
        output.append(total_price)
    else:
        print("none")
print(output)