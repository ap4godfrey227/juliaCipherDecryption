import string

#define functions for shifting values
def rrot(n, d): return(((n >> d)|(n << (8-d)))&0xff)
def lrot(n, d): return((n << d)|(n >> (8 - d)))&0xff


#create list for each possible 12 char XOR key, based off of the shift value
XORkey_chart = ['']*8

for i in range(0,12):
    encrypted_hex_byte = input("What is the encrypted byte: ")
    normal_hex_byte = input("What is the normal byte: ")
	
    #convert the hex bytes to integers for shifting and XORing
    encrypted_int_byte = int("0x" + encrypted_hex_byte, 16)
    normal_int_byte = int("0x" + normal_hex_byte, 16) 

    #create a chart of each possible string of chars, one row per shift value
    for i in range(0, 8):
        shift_value = i+1
        XORkey_int = lrot(normal_int_byte, shift_value) ^ encrypted_int_byte
        XORkey_char = chr(XORkey_int)
        XORkey_chart[i] = XORkey_chart[i] + XORkey_char

#print out shift values and corresponding key
for i in range(0,8):
    print("When shift = " + str(i+1) + ": " + XORkey_chart[i])

#assign the key with complete ascii text
keyshift = int(input("Which shift value will you use for decryption: "))
keyxorasstring = XORkey_chart[keyshift-1]


ciphertext = open("secretfile.txt.gz.enc", "rb").read()

plaintext = []

keyxor = []

#convert the xor key string to int
for i in range(0, 12):
    keyxor.append(ord(keyxorasstring[i]))

#convert the encrypted bytes into ascii text
for i in range(0, len(ciphertext)):
    plaintext.append(rrot((ciphertext[i] ^ keyxor[i % len(keyxor)]), keyshift))

output = open("secretfile.txt.gz", "wb")
output.write(bytes(plaintext))
output.close
