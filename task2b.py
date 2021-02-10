n=int(input("enter the number of elements : "))
a=list(map(int,input("enter the nubers : ").strip().split(",")))#[ :n]
print(list(a))
b=[i for i in a if i>0]
print(list(b))