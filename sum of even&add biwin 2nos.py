# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# i=1
# sum=0
# sum2=0
# while i<=b:
#     if i%2==0:
#         sum=sum+i
#     if i%2!=0:
#         sum2=sum+i
#     i+=1
# print(sum,sum2)

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# sum=0
# sum2=0
# while a<=b:
#     if a%2==0:
#         sum=sum+a
#     else:
#         # i%2!=0
#        sum2=sum2+a
#     a+=1
# print(sum,sum2)
# user=int(input("enter the number:"))
max=-1000
min=0
i=1
while i<=10:
    user=int(input("enter the number:"))
    if user>max:
        max=user
    if user<min:
        min=user
    i+=1
print(max,min)
