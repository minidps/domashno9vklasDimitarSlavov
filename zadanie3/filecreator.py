n=input("How many files do you want to create?")
i=0
while i < int(n):
    i+=1
    f=open(str(i)+"testfile.txt","w")