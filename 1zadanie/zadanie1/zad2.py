grades = [95, 82, 67, 54, 100, 73, 88, 42]
excellent = []
good = []
passed = []
fail = []

for i in grades:
    if(i>=90):
        excellent.append(i)
    if(70<=i<=89):
        good.append(i)
    if(50<=i<=69):
        passed.append(i)
    if(i<50):
        fail.append(i)
print("excellent:")
print(excellent)
print("\ngood:")
print(good)
print("\npassed:")
print(passed)
print("\nfail:")
print(fail)