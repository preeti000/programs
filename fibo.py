a=0
b=1
f=0
n=int(input("enter the number of elements u want to print: "))
print(a)
print(b)
while f<(n-2):
    c=a+b
    print(c)
    temp=b
    a=b
    b=c
    f+=1