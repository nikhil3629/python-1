month_number = int(input("enter month number: "))

if(month_number<1 or month_number>12):
    print("month number is invalid")
else:

    if(month_number == 1):
        print("31")
    elif(month_number == 2):
        print("28 or 29 days")
    elif(month_number == 3):
        print("31")
    elif(month_number == 4):
        print("30")
    elif(month_number == 5):
        print("31")
    elif(month_number == 6):
        print("30")
    elif(month_number == 7):
        print("31")
    elif(month_number == 8):
        print("31")
    elif(month_number == 9):
        print("30")
    elif(month_number == 10):
        print("31")
    elif(month_number == 11):
        print("30")
    elif(month_number == 12):
        print("31")