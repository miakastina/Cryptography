plainText = input("Plaintext: ")
key = int(input("Key: "))

def caesar_encryption(plainText,key):
  encryption_str = ""
  for i in plainText:
    if i.isupper():
      temp_incode = 65 + ((ord(i) - 65 + key) % 26)
      encryption_str = encryption_str + chr(temp_incode)
    elif i.islower():
      temp_incode = 97 + ((ord(i) - 97 + key) % 26)
      encryption_str = encryption_str + chr(temp_incode)
    else:
      encryption_str = encryption_str + i

  print("Ciphertext:",encryption_str)

caesar_encryption(plainText,key)
