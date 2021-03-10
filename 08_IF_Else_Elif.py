#IF | ELSE | ILIF

num1 = int(input("Enter a number:1-->\n"))
num2 = int(input("Enter a number:2-->\n"))
if num1>num2 and num1!=num2:
    print(num1,"is greater than",num2)
elif num2%2==0:
    print(num2,"is even greater & than",num1)
else:
    print(num2,"is odd and greater than",num1)
    