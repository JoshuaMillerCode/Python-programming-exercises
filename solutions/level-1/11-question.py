# Solution

def binary_div_5():
    binarys = [str(x) for x in input(
        "Enter Binary sequence: ").split(",") if int(x, 2) % 5 == 0]
    print(",".join(binarys))


binary_div_5()
