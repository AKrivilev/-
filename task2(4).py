file1 = open('file1.py','r')
m = file1.readlines()
xk=int(list(m[0])[0])
yk = int(list(m[0])[2])
r= int(m[1])
with open("file2.py", "r") as f:
    for line in f:
    	line =list(map(int,line.rstrip().split(',')))
    	if (line[0]- xk)**2 / r**2 + (line[1] - yk)**2 / r**2 < 1:
    	   print("1 - точка внутри")
    	if (line[0]- xk)**2 / r**2 + (line[1] - yk)**2 / r**2 >1: print ("2 точка снаружи")
    	if (line[0]- xk)**2 / r**2 + (line[1] - yk)**2 / r**2 ==1: print ("0 точка на окружности")
    	
file1.close