m = open('e.py' ,'r')
n=list(map(int,m.read().split()))
print (n)
a = sum(n)/len(n)
import math
c = math.ceil(a)
list2= []
for i in n:
	if i <=c:
		list2.append(c-i)
	if i >=c:
		list2.append(i-c)
		
print(sum(list2))
m.close()