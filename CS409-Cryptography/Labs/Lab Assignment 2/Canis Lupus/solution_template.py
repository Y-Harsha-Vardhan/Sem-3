from pwn import *
from Crypto.Util.Padding import pad, unpad

HOST = "0.cloud.chals.io"
PORT = 19966

# Uncomment the 'process' line below when you want to test locally, uncomment the 'remote' line below when you want to execute your exploit on the server
# target = process(["python", "./server.py"])
target = remote(HOST, PORT)

def recvuntil(msg):
    resp = target.recvuntil(msg.encode()).decode()
    print(resp)
    return resp

def sendline(msg):
    print(msg)
    target.sendline(msg.encode())

def recvline():
    resp = target.recvline().decode()
    print(resp)
    return resp

def recvall():
    resp = target.recvall().decode()
    print(resp)
    return resp


recvuntil("IV: ")
IV = bytes.fromhex(recvline())

recvuntil("Flag: ")
flag_enc = bytes.fromhex(recvline())


def validate_padding(iv_hex: str, ciphertext_hex: str) -> bool:
    recvuntil("validated:\n")
    sendline(ciphertext_hex)
    recvuntil("IV:\n")
    sendline(iv_hex)
    response = recvline()
    valid_padding = ("Valid Padding!" in response)
    return valid_padding


# ===== YOUR CODE BELOW =====
# The variable IV has the iv (as a bytes object)
# The variable flag_enc has the ciphertext (as a bytes object)
# You can call the function validate_padding(iv_hex: str, ciphertext_hex: str) -> bool which takes in the hex of the iv (str) and hex of the ciphertext (str) and returns True if the corresponding plaintext has valid padding, and return False otherwise (as dictated by the server's response)

######################################################################################
# Let n = AES.block_size (which we know to be 16)
# In a CBC decryption, P_i = Dec_k(C_i) ^ C_{i-1}
# So, as discussed in the class, if we flip bytes in C_{i-1}, we can influence the last byte of P_i
# Using the validate_padding (oracle), we can test our guesses until we find the correct PKCS#7 padding
# Using this strategy block-by-block, we can recover the plaintext

# First, we need to split the ciphertext into n-byte blocks: C = [C0=IV, C1, C2, ...]
# Then we need to attack each block C_i (with preceding block C_{i-1}) to recover the plaintext
# For each byte (from last to first):
    # Take a guess of C_{i-1} (Forge)
    # Send (C_{i-1}', C_i) to validate_padding
    # If valid padding, deduce the plaintext byte
# Then we will concatenate all recovered plaintext and strip PKCS#7 padding
# The below code implements the discussed strategy:
######################################################################################

n = 16

def split_blocks(data: bytes, size: int = n):
    return [data[ i : i + size] for i in range(0, len(data), size)]

def decrypt_block(prev: bytes, curr: bytes) -> bytes:
    # Decrypting one block using the padding oracle, (validate_padding function)
    intermediate = [0] * n
    plaintext = [0] * n

    for pad_len in range(1, n + 1):
        i = n - pad_len
        found = False

        for guess in range(256):
            # Forging the block (C') to send to the oracle
            forged = bytearray(b'\x00' * n) # Starting with a clean slate

            # For all positions after i, enforcing the correct padding value.
            # We want P'[j] = pad_len, so C'[j] must be intermediate[j] ^ pad_len.
            for j in range(i + 1, n):
                forged[j] = intermediate[j] ^ pad_len

            # For the current position i, inserting our guess.
            forged[i] = guess

            # Checking if this forged block works or not using the validate_padding function
            if validate_padding(forged.hex(), curr.hex()):
                # We got a "Valid Padding" response. Now we verify it's not a false positive.
                # A correct guess should still result in valid padding even if we modify
                # a byte that comes *before* the padding starts.
                
                # Edge case: If i is 0 (we're finding the first byte), there's no preceding
                # byte to modify for a check, so we trust this result.
                if i == 0:
                    is_verified = True
                else:
                    forged_check = bytearray(forged)
                    forged_check[i - 1] ^= 0x01  # Flip a bit in a preceding byte
                    is_verified = validate_padding(forged_check.hex(), curr.hex())

                if is_verified:
                    # The guess is correct! We can now calculate the intermediate and plaintext byte.
                    intermediate[i] = guess ^ pad_len
                    plaintext[i] = intermediate[i] ^ prev[i]
                    found = True
                    break

        if not found:
            raise Exception(f"Byte not found at position {i} with pad_len={pad_len}")

    return bytes(plaintext)

# Decryption
blocks = [IV] + split_blocks(flag_enc, n)
recovered = b""

for i in range(1, len(blocks)):
    plaintext_block = decrypt_block(blocks[i-1], blocks[i])
    recovered += plaintext_block

# Removing the padding:
try:  
    flag = unpad(recovered, n).decode()
except:
    flag = recovered.decode(errors="ignore")

# We get the flag to be: cs409{sid3_ch4nn3l_danger!}
print(f"Flag: {flag}")

# ===== YOUR CODE BELOW =====

target.close()
