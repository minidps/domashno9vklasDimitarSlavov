words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindromes = []

for i in words:
    is_palindrome = True
    for j in range(len(i) // 2):
        if i[j] != i[-(j + 1)]:
            is_palindrome = False
            break
    if is_palindrome:
        palindromes.append(i)
print(palindromes)