from random import randint

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def slice_string(letter, position, text):
    return text[:position] + letter + text[position + 1:]

if __name__ == '__main__':
    print "Enter a 4 letter word: "
    encode_word = raw_input().upper()
    print "Enter 4 numbers: "
    encode_numbers = raw_input()

    new_word = ""
    for i in range(0, 10):
        random_letter = alphabet[randint(0, 25)]
        new_word += random_letter

    for letterIndex in range(0, 4):
        new_word = slice_string(encode_word[letterIndex], int(encode_numbers[letterIndex]) - 1, new_word)

    print new_word

