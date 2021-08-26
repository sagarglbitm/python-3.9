a=int(input("enter no"))
if(a >30):
    print("the value is grater than 30")
elif(a>25 and a<30):
    print(" greater to 25 less to 30")# if two condition are true then it only executed first one
elif(a>27 or a is 27):
    print("greater to 27 and equal to 27")

else:
    print("the value is less than 30")

    #---------------------------------Is and In statement------------------------
b=int(input("enter no"))
if (b is 15): # [if(b==15) and if(b is 15)] both are same
    print("no is 15")
else:
    print("no is not 15")

c=[12,23,34,45]
print(34 in c)    # in statement check whether no is present or not if yes then return true

