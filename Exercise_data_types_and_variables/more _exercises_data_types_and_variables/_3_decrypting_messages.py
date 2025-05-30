key = int(input())
number_of_lines = int(input())
decrypted_message = ''

for letter in range(number_of_lines):
    encrypted_letter_ascii = ord(input())
    decrypted_letter_ascii = encrypted_letter_ascii + key

    decrypted_message += chr(decrypted_letter_ascii)

print(decrypted_message)
