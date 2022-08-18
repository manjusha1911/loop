# binary -decimal conversion
bin=int(input("enter the binary:"))
d=0
i=1
while bin>0:
    rem=bin%10
    d=d+(rem*i)
    i=i*2
    bin=int(bin/10)
print(d)