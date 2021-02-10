n=int(input("enter the no. of terms: "))
a=0
b=1
c=0
if n<0:
    print("please enter a positive number")
    n = int(input("enter the no. of terms: "))
    print("fibonacci series upto ",n,"terms is :")
    while c<n:
       print(a)
       nth=a+b
       a=b
       b=nth
       c+=1

elif n==1:
    print(a)
else:
    print("fibonacci series upto ",n,"terms is :")
    while c<n:
       print(a)
       nth=a+b
       a=b
       b=nth
       c+=1


