#LIST 
l1 = []                 #Empty or Null LIST
l2 = [1,2,3,5,8,11,1,0]            #List of Numbers
l3 = [1,2,3.3,5.6,7,8]  #List of number int& float
l4 = ['a','b','z']      #List of characters
l5 = ['a',5,7.8,"shubham"]#List of Mixed datatypes
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

#LIST FUNCTIONS
l2.sort()
print(l2)
l4.reverse()
print(l4)
l1.append(1)
print(l1)
l2.insert(2,100)
print(l2)
l2.remove(1)  #remove value at index
print(l2)
l2.pop(3)  #pop value at index
print(l2)


#Tuples 

a=()    # It's an example of empty tuple
x=(1,)   # Tuple with single value i.e. 1 
tup1 = (1,2,3,4,5)
tup1 = ('shubham', 5, 'demo', 5.8)

a = 10 
b = 15
print(a,b)     #It will give output as: 10 15
a,b = b,a 
print(a,b)