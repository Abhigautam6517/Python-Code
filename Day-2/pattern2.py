num = int(input("Enter your number"))

for i in range(num,0,-1):
    for j in range(i+1,0 ,-1):
        print("*", end=" ")
    print('')