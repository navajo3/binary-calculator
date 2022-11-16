
def byte(bit, result):
    if bit == 1:
        result = format(result, '08b')
        print("Number in binary: ", result[:8])
        result = hex(int(result, 2))
        print("\nNumber in hexadecimal: ", result[2:])
    elif bit == 16:
        result = format(result, '0128b')
        print("Number in binary: ", result[:128])
        result = hex(int(result, 2))
        print("\nNumber in hexadecimal: ", result[2:])
    else:
        print("Code malfunction: Invalid bit value. Blame the programmer.")
        time.sleep(2)
        exit()