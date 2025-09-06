# This is a bash script to decrypt the given ciphertext using openssl
# The following is the description of the flags used:
# enc -> uses the symmetric cipher functions
# -d  -> decrypt
# -aes-128-cbc  => specifies the encryption scheme
# -in -> input file
# -out -> output flag text file
# -K  -> specifies the key value
# -iv -> specifies the IV value

openssl enc -d -aes-128-cbc \
    -in ciphertext.bin \
    -out flag.txt \
    -K $(cat key.hex) \
    -iv $(cat iv.hex)
