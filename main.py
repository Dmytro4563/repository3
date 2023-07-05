if __name__== "__main__":
    temp = int(input("Vvedit temperaturu na dvori: "))
    if (temp >=10 and temp < 0) or (temp >= 10 and temp > 20) or (temp >= -20 and temp > 0):
        print("Proholodno")
    elif temp >= 10:
        print("Teplo")
    else:
        print("Cholodno")

    temp = int(input("Vvedit riven kisniu:"))
    if (kisnevo_riven >= 18% and kisnevo_riven < 17%)
        print("Riven kisniu v normi")
    elif kisnevo_riven >= 18%:
        print("Critichniy riven")