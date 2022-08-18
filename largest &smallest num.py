i=1
min=1000
max=0
while i<=10:
    user=int(input("enter the number:"))
    if user>max:
        max=user
    if user<min:
        min=user
    i+=1
print(max,min)
