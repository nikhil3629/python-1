angle1 = int(input("enter first angle: "))
angle2 = int(input("enter second angle: "))
angle3 = int(input("enter third angle:"))

if (angle1>0 and angle2>0 and angle3>0 and angle1+angle2>angle3 and angle2+angle3>angle1 and angle3+angle1>angle2 and angle1+angle2+angle3 == 180):

    if(angle1 == angle2 == angle3):
        print("equilateral triangle")
    elif(angle1 == angle2 or angle1 == angle3 or angle2 == angle3):
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("it is not a valid triangle")