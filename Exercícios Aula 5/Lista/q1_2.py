count = 0

for count in range(1,101):
    print(count)
    count+=1
    if count==100:
        print(count)
        while count>0:
            count-=1
            print(count)