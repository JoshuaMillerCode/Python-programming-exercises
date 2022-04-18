# Solution

def binary_div_5():
    binarys = ",".join([str(x) for x in input(
        "Enter Binary sequence: ").split(",") if int(x, 2) % 5 == 0])
    print(binarys)


binary_div_5()
