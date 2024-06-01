import art as duh
print(duh.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text, shift_amount, user_direction):
    encrypted_message = " "
    if user_direction == "encode":
        for letter in user_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                encrypted_message += new_letter
            else: 
                encrypted_message += letter
        print(f"The {user_direction}d text is {encrypted_message}")
        
    elif user_direction == "decode":
        for letter in user_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                encrypted_message += new_letter
            
            else:
                encrypted_message += letter
        
        print(f"The {user_direction}d text is {encrypted_message}")
        

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(user_text = text, user_direction = direction, shift_amount = shift)

    restart_option = input("If you want to go again type 'yes' otherwise type 'no': \n")
    if restart_option == "no":
        should_continue = False
        print("Arrivederci")