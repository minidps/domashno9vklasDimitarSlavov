#tova e funkciq, kojto wrushta n-toto chislo of fibonachi
def fibonachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
#tova e funkciq, kojto wrushta n-toto chislo of fibonachi izpolvashta rekursiq
def fibonachi_recursive(n, a=0, b=1):
    if n==0:
        return a
    else:
        return fibonachi_recursive(n-1, b, a+b)
    
print(fibonachi(10))
print(fibonachi_recursive(10))