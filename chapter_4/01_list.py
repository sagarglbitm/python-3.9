a=[1,"apple",2.35,'s'] #list are a container to store a set of value of any data types
print(a)
print(a[0]) # list indexing start with 0th index
a[0]=2 # list can be modified
print(a)
print(a[-1]) # it is same as a[3] as negative sign start from 
# backwordwith index a[-1] and from right hand side to 
# left hand side incremented but with negative sign

# list slicing
b=[10,20,30,40,50,60]
print(b[0:3])# it print from 0th index to 2nd index
print(b[-3:-1]) # it is same as b[3:5]
print(b[1:]) # it start print with index 1st to last index