a = int(input('enter number : '))
i = 0
num = 1
while i<a:
    num+=1
    count = 0
    for j in range(1,num):
        if num%j==0:
            count+=1
        if count>2:
            break
    if count==1:
        i+=1
print(num)
