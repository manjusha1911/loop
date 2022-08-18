# febonacci number/febonacci sequence:
# Each number is sum of precedingtwo numbers starting from 0,1
# ex: 0,1
# 0+1=1
# 1+1=2
# 1=2=3
# 2+3=5
# 3+5=8
# 5+8=13
# 8+13=21

max=10
n1=0
n2=1
n3=n1+n2
i=0
while i<=max:
    print(n1)
    n1=n2
    n2=n3
    n3=n1+n2
    i+=1
