alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# The .index function searches for a specific value, item, or character within a list, string, or DataFrame, and returns its exact numerical position (its "index").

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def encrypt(original_text, shift_amount):
    cypher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount #(we used alphabet.index(letter)
        # to find the shifted       position for each letter chosen. -index tells us where the letter is
        # next, we create a letter by using the alphabet list using the square bracket and tap into the item at the shifted_position.
        cypher_text += alphabet[shifted_position] # we'll need an empty string to accumulate the letters so they won't reset each time the code runs
        shifted_position %= len(alphabet)
    print(f"Here is the encoded result: {cypher_text}")
        
encrypt(text, shift)
    
# def encrypt(original_text, shift_amount):
#     encrypt_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)# makes sure we're always within the range of 25
#         encrypt_text += alphabet[shifted_position]
#
#
#     print(f"Here is the encoded result {encrypt_text}")

# Whe you modulo(%) something, it gives you the remainder as your output.
# Eg, 34 % 25 give you 9 as the remainder. 9(shift amount) + 25(total alphabets) = 34





# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
