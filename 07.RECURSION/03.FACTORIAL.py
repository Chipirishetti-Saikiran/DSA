def factorial(n):
    if n==0 or n==1:
        return 1
    #recursive 
    return n*factorial(n-1)

print(factorial(5))

