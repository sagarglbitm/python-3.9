# print("hello world")
# print("sagar")

# single line comment


# ''' multi
#     line
#     comment'''

# print('''twinkle litttle star 
# twinke'''
# ) # it is used when we have multi line statement,which takes two or more line then use single_quote
s =int(input())
a=[]
for i in range (0,s) : 
    p=int(input())
    a.append(p)
a.sort() 
a.reverse()#6,6,5,3,2
for i in range (0,s):
    if(a[i]>a[i+1]):
        print(a[i+1])
        break; 

