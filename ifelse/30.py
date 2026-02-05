week = int(input("enter week number: "))

if(week >= 7):
    print("invalid week number")
else:
    if(week == 0):
        print("sunday")
    elif(week == 1):
        print("monday")
    elif(week == 2):
        print("tuesday")
    elif(week == 3):
        print("wednesday")
    elif(week == 4):
        print("thursday")
    elif(week == 5):
        print("friday")
    else:
        print("saturday")