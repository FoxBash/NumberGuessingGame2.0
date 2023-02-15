import random

print("This is a guess game and ill be giving you hints along the way")
n = int(input("Enter starting point"))
c =int(input("Enter Ending point"))

count = 0
def game(x,n,c):
    global count
    count +=1
    g = int(input("Enter the input"))
    if g == x:
        print("\n\nYou win!!! in just "+ str(count) +" moves")
        return
    elif g > x and g > n and g < c:
        print("Thats too big")
        game(x,n,c)
    elif g < x and g > n and g < c:
        print("Thats too low")
        game(x,n,c)
    else:
        print("Check on input:(")
        game(x,n,c)


if n < c:
    x = random.randint(n,c)
    game(x,n,c)
else:
    v = n
    n = c
    c = v
    x = random.randint(n,c)
    game(x,n,c)