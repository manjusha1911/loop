# average:
# add up all of the numbers and then divide by how many numbers are there 
# ex:
# 1,2,3,4,5,6,7,8,9,10::::: total 10 numbers
# 1+2+3+4+5+6+7+8+9+10=55 :total sum of numbers
# 55/10
i=1
sum=0
while i<=10:
    user=int(input("enter the number:"))
    sum=sum+user
    i+=1
average=sum/10
print(average)


