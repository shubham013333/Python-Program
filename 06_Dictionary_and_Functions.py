#DICTIONARY AND FUNCTIONS
dic = {"shubham":1,"vijay":2,"juned":3}
print(dic) 
print(type(dic))    #type <dict>
print(dic.keys())  #print key values 
print(dic.items())   #print itemsWithValues
dic2 = dic.copy()
print(dic2)     #print the copy of previous dictionary 
dic2.update({"sagar":4})
print(dic2)

print(dic2["vijay"])
