# 9:00PM 8/11/22

running = 1
loop = 1
result = 0

def main():
    global loop, result
    b1 = input("Number1: ")
    n1 = int(b1, 2)
    print(n1)
    while loop == 1:
        calc = input("Add or Subtract(A/S): ").lower()
        if calc == "a":
            loop = 0
            continue
        elif calc == "s":
            loop = 0
            continue
        else:
            print("Not valid input")
            continue
    b2 = input("Number2: ")
    n2 = int(b2, 2)
    print(n2)
    if calc == "a":
        result = n1 + n2
        return 
    elif calc == "s":
        result = n1 - n2
        return

def extra():
    global result
    ce = input("Continue or End (C/E): ").lower()
    if ce == "c":
        return
    elif ce == "e":
        result = format(result ,"b")
        print("Your number in binary is: ", result)
        return

def calc():
    while loop == 0:
        calc = input("Add or Subtract(A/S): ").lower()
        if calc == "a":
            loop = 1
            continue
        elif calc == "s":
            loop = 1
            continue
        else:
            print("Not valid input")
            continue

### defo not done

main()
extra()

    
        

    

