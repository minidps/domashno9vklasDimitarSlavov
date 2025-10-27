import random
n=random.randint(1,10)
print("There must be",n,"files in the folder")
i=0
while i < int(n):
    i+=1
    f=open(str(i)+"testfile.txt","w")