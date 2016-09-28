x = True  # flag
y = input("Please enter some value to check ")
y = int(y)
a = False # flags
b = False # flags
while x:
    
    print("value of y")
    print(y)
    if not y % 2:
        a = True
        y += 1
    else:
        a = False
        y += 1
        continue

    if y > 50:
        b = True
    else:
        b = False
        y += 1
        continue

    if a and b:
        x = False

    y += 1
        