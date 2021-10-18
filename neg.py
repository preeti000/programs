list=[]
n=int(input("enter the no. of elements: "))
print("enter the elements")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
res=[j for j in list if j>=0]
print(res)