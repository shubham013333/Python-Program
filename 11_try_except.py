#TRY AND EXCEPT 

num1 = input("enter number 1")
num2 = input("enter number 2")
try:
    print("sum of numbers is")
    print(int(num1)+int(num2))
except Exception as e:
    print(e)

print("this is important line")    