cipherText = raw_input("Ciphertext: ")
key = int(raw_input("Key: "))

def caesar_decryption(cipherText,key):
  decryption_str = ''
  for i in cipherText:
    if i.isupper():
     if ((ord(i) - 65 - key) < 0):
      temp_incode = 65 + ((ord(i) - 65 - key + 26) % 26)
     else:
      temp_incode = 65 + ((ord(i) - 65 - key) % 26)
     decryption_str = decryption_str + chr(temp_incode)
    elif i.islower():
     if ((ord(i) - 97 - key) < 0):
      temp_incode = 97 + ((ord(i) - 97 - key + 26) % 26)
     else:
      temp_incode = 97 + ((ord(i) - 97 - key) % 26)
     decryption_str = decryption_str + chr(temp_incode)
    else:
     decryption_str = decryption_str + i

  print "Plaintext:",decryption_str

caesar_decryption(cipherText,key)
