temperature = float(
    input("Please Enter The Temperature. Input Can Be C or F "))
unit = input("Please Enter The Unit You Want To Convert! C or F ")

if unit == "C":
    print((temperature * 9/5) + 32)
elif unit == "F":
    print((temperature - 32) * 5/9)
