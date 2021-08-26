def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

p=5
factorial=fact(p)
print(factorial)
#----------------------------------------------------------
print("how" , end=" ") # it will print in one line otherwise all print in next line
print("are" , end=" ")
print("you ?" , end=" ")



    