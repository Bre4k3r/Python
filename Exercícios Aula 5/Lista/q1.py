count = 0

for count in range(1,100):
    print(count)
    count+=1
    if count==100:
        for count in range(100,0,-1):
            print(count)
            count-=1

