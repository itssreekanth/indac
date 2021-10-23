num = 0
result = True
while result:
    num+=1
    for i in range(2,21,2):
        if num%i==0:
            if i==20:
                result = False
            else:
                continue
        else:
            break
print(num)
