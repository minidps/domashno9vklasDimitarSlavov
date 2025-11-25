def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

a = [1, 6, 4, 7, 2]

print(sum_of_list(a))
print(recursive_sum(a))