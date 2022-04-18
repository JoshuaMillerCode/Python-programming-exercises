# My Solution
# akjsdhfjlkashdfkjasdhfkjashfdkjhaskjfhjkashfkjahsdfjkhaskdjfhakjshfjkasdhfkjhaskjfhasjkdfh
words = [x for x in input().split(" ")]

tracker = {}

for word in words:
    if word in tracker:
        pass
    else:
        tracker[word] = 1

print(" ".join(sorted([*tracker])))
