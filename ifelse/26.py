num = int(input("enter a number: "))

if(num%5 == 0 and num%11 == 0):
    print(f"{num} is divisible by 11 and 5")
else:
    print(f"{num} is not divisible by 11 and 5")