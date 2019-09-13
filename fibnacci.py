a=0
b=1
n=int(input("enter number"))
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)