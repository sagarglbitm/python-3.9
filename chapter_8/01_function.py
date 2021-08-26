def percent(mark):
    return((mark[0]+mark[1]+mark[2]+mark[3])/400)*100
marks1=[10,20,30,40]
percentage=percent(marks1)
print(percentage)  
#----------------------------------------------------
def greet(name="roshan"):#default arg,when no arg passed then dfault arg passed otherwise arg passed
    print("hello "+name)

greet("sagar")# when we pass arg then it default arg is not called
greet()# when we not pass any arg tdefault arg called