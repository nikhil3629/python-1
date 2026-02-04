telugu = int(input("enter telugu marks: "))
hindi = int(input("enter hindi marks: "))
english = int(input("enter english marks: "))

total = telugu+hindi+english

if(total>270):
    print("A Grade")
elif(240<total<=270):
    print("B Grade")
else:
    print("c Grade")