# f = open("shubham.txt", "w")
# a = f.write("my hobby is playing football\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("my hobby is playing cricket\n")
# print(a)
# f.close()


# Handle read and write both
f = open("shubham.txt", "r+")
print(f.read())
f.write("thank you")
  
