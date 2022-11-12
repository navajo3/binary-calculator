def byte():
    if bit == 1:
        result = format(result, '08b')
    elif bit == 16:
        result = format(result, '0128b')
    else:
        print("Code malfunction: Invalid bit value. Blame the programmer.")
        time.sleep(2)
        exit()