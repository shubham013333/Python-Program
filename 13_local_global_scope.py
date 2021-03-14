#LOCAL SCOPE
def sum():

      a=10 #local variable cannot be accessed outside the function
      b=20
      sum=a+b
      print( sum)

print(a) #this gives an error

#GLOBAL SCOPE
a=1  #global variable

def print_Number():

            a=a+1;
            print(a)

 print_number()