a=int(input("enter the number:"))
product=1
while a>0:
    product=product*(a%10)
    a=a//10
print("product of the digits",product)