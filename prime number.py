# prime number:   A number that id divisible only by itself and 1  
# ex: 13 is a prime number
# 1,2,3,4,5,6,7,8,9,10,11,12,13.
# 1%13==0
# 2%13!=0
# 13%13==0
# not a prime number
# ex: 6
# 1,2,3,4,5,6.
# 1%6==0
# 2%6==0
# 3%6==0
# 4%6!=0
# 5%6!=0
# 6%6==0
n=int(input("enter the number:"))
count=0
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i+=1
if count==2:
    print(n,"is a prime number")
else:
    print(n,"not a prime number")



