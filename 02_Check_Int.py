import random


def check_v1():
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

def check_v2():
    x = random.randint(10, 100)
    x = x / random.randint(1, 10)

    print(x)

    if x == int(x):
        print("true")

    else:
        print("failed")

    return x


while True:
    print("""
    
    
    """)
    go = input("go? ")
    if go == "y":
        g = check_v2()