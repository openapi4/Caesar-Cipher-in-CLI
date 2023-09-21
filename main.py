alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def keep_shift_in_alphabet(shift_amount):
    new_shift_amount = shift_amount % 26
    return new_shift_amount


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}\nWith key = {user_shift}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
user_shift = int(input("Type the key (shift number):\n"))
shift = keep_shift_in_alphabet(user_shift)

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)