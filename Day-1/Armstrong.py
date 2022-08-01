user_digit = int(input("Enter your Number : "))
temp = user_digit;
sum = 0;

while temp>0:
    last_digit = temp%10
    sum = sum+(last_digit*last_digit*last_digit) 
    temp = temp//10

if(user_digit==sum):
    print("This is ArmsStrong Number")
else:
    print("not Armsstrong Number")
   
