max = float("-inf")

for i in range(5):
    num = int(input(f"Enter a number {i+1}:"))
    if num>max:
        max=num
        
    
print("max number:",max)