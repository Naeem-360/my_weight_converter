
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "L":
    converted = weight / 0.45
    print("Weight in Lbs: ", converted)
else:
    converted = weight * 0.45
    print("Weight in Kg: ", converted)
