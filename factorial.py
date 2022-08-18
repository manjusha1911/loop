# factrorial number:    (factrorial of "0 value" is "1")
# factrorial of a number is the product of all integers between 1 and itself.
# ex:4
# 4=4*3*2*1=24

# i=int(input("enter the number:"))
# fact=1
# while i>0:
#     fact=fact*i
#     i-=1
# print("factorial:",fact)
i=1
fact=1
while i<=5:
    fact=fact*i
    i+=1
print("factorial:",fact)
