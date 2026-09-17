#create a menu driven calculator 

def add(a, b):
    print("sum",a + b)

def sub(a,b):
    print("sub",a-b)

def mul(a, b):
    print("mul",a*b)

def div(a, b):
    print("div", a/b)

def mod(a,b): 
    print(a // b)

while True:
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. modulas")
    print("6. exit")

    a=int(input("enter first number"))
    b=int(input("enter second number"))
    choice=int(input("enter choice"))

    match choice:
        case 1:
             add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
        case 5:
            mod(a,b)
        case 6:
            print("Program exited")
            break
        case _:
            print("Invalid choice")
