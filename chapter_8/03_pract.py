# sum of first 10 natural no 
def sum(n):
    if n>=0:
        return n + sum(n-1) 

p=10
natural=sum(p)
print(natural)