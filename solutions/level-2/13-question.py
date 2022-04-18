
def letters_and_digits():
    sentence = [word for word in input("Enter sentence: ")]
    letters = 0
    digits = 0
    for char in sentence:
        if (char.isdigit()):
            digits += 1

        elif (char.isalpha()):
            letters += 1

    print("LETTERS " + str(letters) + " DIGITS " + str(digits))


letters_and_digits()
