#tazi funkciq obrushta spisuk izpolzvaiki slicing
def flip_list(lst):
    return lst[::-1]
#tazi funkciq obrushta spisuk izpolzvaiki rekursiq
def flip_list_recursion(lst):
    if not lst:
        return lst
    else:
        return lst[-1] + flip_list_recursion(lst[:-1])

a="Hello"

print(flip_list(a))
print(flip_list_recursion(a))
