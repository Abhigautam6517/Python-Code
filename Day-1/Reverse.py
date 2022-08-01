num = 1234
# num = int(input("Enter your digit"))
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse is",rev)