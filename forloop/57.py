num = int(input("enter a number:"))

for i in range(len(str(num))):
    rem=num%10
    if rem%2 == 0:
        print(rem)
    num=num//10


