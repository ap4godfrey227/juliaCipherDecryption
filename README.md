# juliaCipherDecryption
A decryption program for a cipher algorithm provided by my professor.

The cipher involved taking a text file with ascii characters and applying the following algorithm to encrypt it:

enc_char = bit_rotate(plain_char, N) xor key_byte

For this part of the project, we were only told that the key_byte was 12 characters long, all being from the english alphabet.Everything else we needed to find ourselves.

To find the key, I created a text file with an identical name to the encrypted zip file (which contained the encrypted ciphertext), zipped the file, and then compared the hex dumps to look for similarities in the values. Once I found bytes that were supposed to match up, I began the decryption process, which was simply the inverse of his encryption algorithm, keeping order of operations in mind.

To ensure my answer was correct, I unzipped my output file and compared the sha512sum values of my unzipped file and the initial plaintext, which was also provided by the professor.
