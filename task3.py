from collections import Counter
import operator
string=input("enter a string : ")
freq=Counter(string)
a=dict(freq)
sorted_a=sorted(a.items(), key=operator.itemgetter(1), reverse=True)
b=dict(sorted_a)
for key,value in b.items():
   print(key, ":" ,value)
