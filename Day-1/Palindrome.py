num = 121
rev = 0
temp = num

while(temp!=0):
    digit = temp%10
    rev = rev*10 + digit
    temp = temp//10

if num==rev:
    print("your number is Palindrome")
else:
    print("Your number is not palindrome")