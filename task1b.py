fn=input("enter a file name : ")
extn=fn.split(".")
b=(extn[-1])
mdict=dict([('py', 'python'), ('txt', 'text'), ('docx', 'document')])
c=mdict.get(b)
if c==None:
    print("The extension of the file is : ",b)
else:
    print("The extension of the file is : ",c)