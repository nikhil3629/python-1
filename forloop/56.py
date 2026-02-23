num = int(input("enter a number:"))
for i in range(len(str(num))):
    rem = num%10
    print(rem)
    num=num//10