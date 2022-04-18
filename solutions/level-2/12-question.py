
def both_even():
    nums = range(1000, 3001)
    even_list = []
    for x in nums:
        x_str = str(x)
        if (int(x_str[0]) % 2 == 0 and int(x_str[1]) % 2 == 0 and int(x_str[2]) % 2 == 0 and int(x_str[3]) % 2 == 0):
            even_list.append(x_str)
    return ", ".join(even_list)


answer = both_even()

print(answer)
