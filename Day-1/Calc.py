from ast import operator


value1 = int(input("Enter your First Value: "))
# print("Enter your operator /, + , - , * : ")
opr = input("Enter your operator /, + , - , * : ")

value2 = int(input("Enter your second Value: "))


if(opr=="/"):
    print("your Answer is ", value1/value2);
elif(opr=="*"):
    print("your Answer is ", value1*value2);
elif(opr=="+"):
    print("your Answer is ", value1+value2);

elif(opr=="-"):
    print("your Answer is ", value1-value2);
