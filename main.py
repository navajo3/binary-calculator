# source code
import time
import bytefunc

loop = 0
result = 0

def main():
    global loop, result, bit
    while loop == 0:
        bit = int(input("Byte format (1/16): "))
        if bit == 1:
            loop = 1
            continue
        elif bit == 16:
            loop = 1
            continue
        else:
            continue
    while loop == 1:
        b1 = input("Number1: ")
        if (set(b1) | {'0', '1'}) == {'0', '1'}:
            loop = 0
            continue
        else:
            print("Number is not binary")
            continue
    n1 = int(b1, 2)
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
    while loop == 1:
        b2 = input("Number2: ")
        if (set(b2) | {'0', '1'}) == {'0', '1'}:
            loop = 0
            continue
        else:
            print("Number is not binary")
            continue
    n2 = int(b2, 2)
    if calc == "a":
        result = n1 + n2
        return 
    elif calc == "s":
        result = n1 - n2
        return
    else:
        print("Code malfunction: Invalid calculation value. Blame the programmer.")
        time.sleep(2)
        exit()

def extra():
    global result
    ce = input("Continue or End (C/E): ").lower()
    if ce == "c":
        return
    elif ce == "e":
        bytefunc.byte(bit, result)
        time.sleep(2)
        exit()
    print("Your number in binary is: ", result)
    time.sleep(2)
    exit()

def calc():
    global loop, result
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
    while loop == 1:
        b3 = input("Number: ")
        if (set(b3) | {'0', '1'}) == {'0', '1'}:
            loop = 0
            continue
        else:
            print("Number is not binary")
            continue
    n3 = int(b3, 2)
    if calc == "a":
        result = result + n3
        return
    elif calc == "s":
        result = result - n3
        return
    else:
        print("Code malfunction: Invalid calculation value. Blame the programmer.")
        time.sleep(2)
        exit()

main()

while loop == 0:
    extra()   
    calc()