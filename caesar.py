def caesar_cipher(text, mode):
  """Encrypts or decrypts text using a Caesar Cipher with a fixed shift value.

  Args:
      text: The text to encrypt or decrypt.
      mode: 'encrypt' or 'decrypt'

  Returns:
      The encrypted or decrypted text.
  """
  # Set a fixed shift value (replace with your desired shift)
  shift = 3  
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  result = ''

  for char in text:
    if char.isalpha():
      if mode == 'encrypt':
        index = alphabet.find(char.lower())
        new_char = shifted_alphabet[index]
      else:
        index = shifted_alphabet.find(char.lower())
        new_char = alphabet[index]
      result += new_char.upper() if char.isupper() else new_char
    else:
      result += char
  return result

# Get user input
message = input("Enter a message: ")
mode = input("Enter 'encrypt' or 'decrypt': ")

# Perform encryption or decryption
if mode == 'encrypt':
  encrypted_message = caesar_cipher(message, mode)
  print("Encrypted message:", encrypted_message)
else:
  decrypted_message = caesar_cipher(message, mode)
  print("Decrypted message:", decrypted_message)
