# 9:00PM 8/11/22
import time

exemption = [0, 1]

running = 1
loop = 0
result = 0

def main():
    global loop, result
    while loop == 0:
        b1 = input("Number1: ")
        if b1 == type(str) and not any(exemption):
            print("Not a binary number")
        
    n1 = int(b1, 2)
    print(n1) ## REMOVE THESE ONCE DONE
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
    print(n2) ## REMOVE THESE ONCE DONE
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
        result = format(result ,"b")
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
    b3 = input("Number: ")
    n3 = int(b3, 2)
    print(n3) ## REMOVE THESE ONCE DONE
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

while running == 1:
    extra()
    calc()

    
        

    

