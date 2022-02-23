n=int(input (' введите количество элементов массива: '))
m = int(input('введите шаг:'))

list1 = list(range(1,n+1, 1))
list2= list1*2
i = 1

while True:
	print(i, end=' ')
	list2=list2+list1
	i = list2[int(m-1+list2.index(i))]
	if i==1:
		break
		
