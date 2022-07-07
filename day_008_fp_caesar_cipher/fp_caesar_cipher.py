# CAESAR CIPHER

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
my_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
my_text = input("Type your message:\n").lower()
my_shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    text = text.lower()    
    initial_indexes = []
    shifted_indexes = []
    message = ""

    for letter in text:
        letter_index = alphabet.index(letter)
        initial_indexes.append(letter_index)
        
    for num in initial_indexes:
        if direction[0] == "e":
            if num + shift > 25:
                if shift > 25:
                    shift = shift % 26
                num = (num + shift) - 26
            else:
                num += shift
        elif direction[0] == "d":
            if num - shift < - 26:
                if shift > 26:
                    shift = shift % 26
                num = (num - shift) + 26
            else:
                num -= shift
        shifted_indexes.append(num)
        
    for num in shifted_indexes:
        letter = alphabet[num]
        message += letter
        
    if direction[0] == "e":
        print(f"The encrypted message is '{message}'.")
    elif direction[0] == "d":
        print(f"The decrypted message is '{message}'.")


caesar(text = my_text, direction = my_direction, shift = my_shift)
