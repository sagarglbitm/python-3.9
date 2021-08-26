a=int(input())
for i in range(1,a): 
    print(i)
    if i==5:
        break
else: # else part is run when loop is exit by naturally not by break 
    # therefore else_part is also not executed
    print("value of i is not in range of 8")