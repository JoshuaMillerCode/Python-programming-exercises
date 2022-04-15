# Solution
import math
# Formula: Q = Square root of [(2 * C * D)/H]

# work in progess.


def weird_formula():
    D = input("Enter number: ")
    C = 50
    H = 30
    nums = D.split(",")
    ls = []
    for x in nums:
        calc = 2 * C * float(x) / H
        sqrt = int(math.sqrt(calc))
        ls.append(str(sqrt))
    print(", ".join(ls))


weird_formula()
