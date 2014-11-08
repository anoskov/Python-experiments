from recursion import Recursion

@Recursion
def fact(n, result=1):
    if n <= 0:
        return result
    else:
        return fact.call(n - 1, result * n)

print(fact(100000))