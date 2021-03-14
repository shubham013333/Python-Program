#___________
#Recursion |
#___________


def factorial_iterate(n):
    fact=1 
    for i in range(n):
        fact*=i+1
    return fact
        
def factorial_recusion(n):
    if n==1:
        return 1 
    else:
        return n*factorial_recusion(n-1)
        
print(factorial_iterate(4))
print(factorial_recusion(5))