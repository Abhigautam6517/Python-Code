user = int(input("Enter your digit: "))
temp = user

count = 0

while(temp>0):
    digit = temp%10
    if(digit==0):
        count+=1   
    temp = temp//10
print("count is",count)   

