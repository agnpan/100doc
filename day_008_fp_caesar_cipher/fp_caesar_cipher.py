# CAESAR CIPHER

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(text, shift, direction):
    text = text.lower()    
    initial_indexes = []
    shifted_indexes = []
    message = ""

    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            initial_indexes.append(letter_index)
        else:
            initial_indexes.append(letter)
        
    for num in initial_indexes:
        if direction[0] == "e":
            if type(num) == int:
                if num + shift > 25:
                    if shift > 25:
                        shift = shift % 26
                    num = (num + shift) - 26
                elif num + shift <= 25:
                    num += shift
        elif direction[0] == "d":
            if type(num) == int:
                if num - shift < -26:
                    if shift > 26:
                        shift = shift % 26
                    num = (num - shift) + 26
                elif num - shift >= -26:
                    num -= shift
        shifted_indexes.append(num)
        
    for num in shifted_indexes:
        if num in range(-26, 26):
            letter = alphabet[num]
            message += letter
        else:
            message += str(num)
        
    if direction[0] == "e":
        print(f"The encrypted message is '{message}'.")
    elif direction[0] == "d":
        print(f"The decrypted message is '{message}'.")


retry = True
while retry:
    my_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    my_text = input("Type your message:\n").lower()
    my_shift = int(input("Type the shift number:\n"))
    caesar(text=my_text, direction=my_direction, shift=my_shift)
    retry_prompt = input("Would you like to retry (y/n)? ").lower()
    if retry_prompt[0] == "n":
        retry = False
    else:
        print()
        continue
