import random


def hi():
    x = random.randint(10, 100)
    x = x / random.randint(1, 10)

    print(x)

    int_check = isinstance(x, int)
    print(int_check)
    if int_check:
        print("true")

    else:
        print("failed")

    return x

while True:
    print("""
    
    
    """)
    go = input("go? ")
    if go == "y":
        g = hi()