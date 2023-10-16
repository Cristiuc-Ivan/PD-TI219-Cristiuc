x = int(input("Enter a number from 1 to 9: "))

if x in range(1, 4):
    s = str(input("Enter a string: "))
    n = int(input("Enter number of string repeats: "))
    for i in range(n):
        print(s)
elif x in range(4, 7):
    m = int(input("Enter a power: "))
    print(x ** m)
elif x in range(7, 10):
    for i in range(10):
        x += 1
        print(x)
else:
    print("Error of input! Enter a valid number from 1 to 9")
