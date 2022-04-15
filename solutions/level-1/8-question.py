# Solution

input_str = input("Enter words sep commas:  ")

word_list = input_str.split(',')
sort = sorted(word_list)
print(",".join(sort))
