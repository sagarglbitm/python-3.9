a={}
print(type(a)) # it sows that it is a empty dictionary not a set
b=set()
print(type(b)) # it shows that it is a empty set
b.append(2) # here we can add element by using add funcn but it takes only one arg.
b.add(4)
# b.add([60,70]) here we cannot add list into asets bcz list can be done [changing /hashable]
b.add((60,70)) #here we can add tple into sets  bcz tuple cannot be done [changes /hashable]
#b.add({60:70}) #here we cannot add dictionary into sets  bcz dictionary can be done changes
print(b) # it print the sets,which is {2,4}
