from Crypto.Cipher import AES

# The value of the block size used in Encryption
n = AES.block_size
# This is the header given to us in the encryptor.py
HEADER = "_Have you heard about the \{quick\} brown fox which jumps over the lazy dog?\n__The decimal number system uses the digits 0123456789!\n___The flag is: "

# Reading the ciphertext.bin
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()

# Based on the encryption scheme used in encryptor.py, we know the following info:
# The plaintext is modified to have each character repeated AES.block_size times
# So, because the AES is in MODE_ECB, we know that each block of the ciphertext will be 1 block per character of the plaintext
# Also, we know that the ECB encrypts each block independently, so if two plaintext blocks are same, their ciphertext blocks will also be identical
# Since we know the HEADER, we can come up with this attack:

# First we split the ciphertext into n-byte blocks
blocks = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]

# Then we can build a mapping from known HEADER to the unknown plaintext
mapping = {}
for i, ch in enumerate(HEADER):
    mapping[blocks[i]] = ch

# Recovering the flag characters from the mapping
flag = ''.join(mapping[b] for b in blocks[len(HEADER):])

# Using this attack, we get the flag to be: cs409{r3dund4nt_l34k4g35}
print("Flag:", flag)
