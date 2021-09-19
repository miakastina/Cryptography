alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plainText = raw_input("Plaintext (capital letters w/o spaces): ")
key = int(raw_input("Key (number): "))
n = len(plainText)
cipherText = ""

for i in range(n):
    c = plainText[i]
    loc = alpha.find(c)
    newloc = (loc + key)%26
    cipherText += alpha[newloc]
    print c,"=>",'(',loc,'+',key,') mod 26 =', newloc,'=>',alpha[newloc]

print "\nCiphertext:",cipherText
