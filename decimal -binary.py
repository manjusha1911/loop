
# decimal-Binary
dec=int(input("enter the  number:"))     
bin=0
sum=1
while dec>0:
    rem=dec%2
    bin=bin+(rem*sum)
    sum=sum*10
    dec=int(dec/2)
    print(rem)