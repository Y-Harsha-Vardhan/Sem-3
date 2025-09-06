from pwn import *
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

HOST = "0.cloud.chals.io"
PORT = 11437

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


def choice1(params: str) -> str:
    recvuntil("parameters: ")
    sendline("1")
    recvuntil("parameters: ")
    sendline(params)
    recvuntil("hex): ")
    ciphertext_hex = recvline().strip()
    return ciphertext_hex

def choice2(params_enc: str) -> tuple[bool, str]:
    recvuntil("parameters: ")
    sendline("2")
    recvuntil("hex): ")
    sendline(params_enc)
    resp = recvline().strip()
    if resp == "Invalid parameters! Incorrect padding or Non-ASCII characters detected!":
        recvuntil("hex): ")
        return False, recvline().strip()
    elif resp == "Your parameters have been successfully submitted!":
        return False, ""
    elif resp == "Welcome, admin!":
        recvuntil("flag: ")
        return True, recvline().strip()
        


# ===== YOUR CODE BELOW =====
# Use the function choice1(params) the send your parameters (str) to the server (Choice 1)
# It returns (given that your input was successfully processed) the ciphertext as a hex-string
#
# Use the function choice2(params_enc) to send your encrypted parameters (hex string) to the server (Choice 2)
# It returns a 2-tuple: the first component being a boolean indicating whether you got admin access (True) or not (False), the second component being the hex-string returned by the server (empty string in the case that the server returns nothing)

############################################

# Given that the key is the same as the IV. Using this vulnerability, we can come up with an attack
# Suppose we have a ciphertext C which consists of blocks: C0, C1, C2 ...  
# Let n = AES.block_size (The length of each ciphertext block)

# When we decrypt the first block C0, we get P0 = Dec(C0)^IV = Dec(C0)^k (as given that IV = key)
# If we can get the server to decrypt C = C0 || 0^n || C0
# The ciphertext blocks after decryption will be: 
# P0 = Dec(C0)^k
# P1 = Dec(C1)^C0 
# P2 = Dec(C0)^C1 = Dec(C0) ^ (0^n) = Dec(C0)
# So, P0^P2 gives the key (= IV), using which we can find the entire plaintext

# The below code utilizes the above mentioned idea to find the flag

############################################

n = AES.block_size

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x^y for x, y in zip(a, b)])

# Choosing a simple plaintext to get a ciphertext:
cipher_HEX = choice1("a=b")
cipher = bytes.fromhex(cipher_HEX)

C0 = cipher[:n] # The first block of the ciphertext

# Now creating a malicious ciphertext which uses the above mentioned structure
mal = C0 + (b"\x00" * n) + C0
mal_HEX = mal.hex()

# Sending this to the server:
ok, leaked_HEX = choice2(mal_HEX)
assert not ok and leaked_HEX != "" # Ensuring that we got a HEX back
leaked = bytes.fromhex(leaked_HEX)

# Finding the key
P0 = leaked[:n]
P2 = leaked[n*2 : n*3]
key = xor_bytes(P0, P2)


# After this our task is relatively simple
# We need to first encrypt a payload containing "admin=true" using the obtained key
# then make the server decrypt it to get the key
payload = "a=b&admin=true"
payload_bytes = payload.encode()

padded_payload = pad(payload_bytes, n)

cipher_loc = AES.new(key, AES.MODE_CBC, iv=key)
forged_cipher = cipher_loc.encrypt(padded_payload)
forged_cipher_HEX = forged_cipher.hex()

# Sending this to the server, we get back the encrypted flag
got, enc_flag = choice2(forged_cipher_HEX)

# Now we need to decrypt this flag
flag_cipher = bytes.fromhex(enc_flag)
cipher_loc = AES.new(key, AES.MODE_CBC, iv=key)
flag = unpad(cipher_loc.decrypt(flag_cipher), n).decode()

# Using this method, we get that the flag is: cs409{fu11_k3y_recovery_ftw_1mpl3m3nt_w1th_c4r3}
print(f"Flag: {flag}")
"""
This is the obtained output when this code is run:
[x] Opening connection to 0.cloud.chals.io on port 11437
[x] Opening connection to 0.cloud.chals.io on port 11437: Trying 64:ff9b::a5e3:d21e
[+] Opening connection to 0.cloud.chals.io on port 11437: Done
Do you want to 1) encrypt parameters, or 2) submit parameters: 
1
Enter parameters: 
a=b
Encrypted parameters (hex): 
de774f587fc2e076ae2837844444c146


Do you want to 1) encrypt parameters, or 2) submit parameters:
2
Enter encrypted parameters (in hex): 
de774f587fc2e076ae2837844444c14600000000000000000000000000000000de774f587fc2e076ae2837844444c146
Invalid parameters! Incorrect padding or Non-ASCII characters detected!

Invalid Decryption Result (hex):
613d620d0d0d0d0d0d0d0d0d0d0d0d0dcada817e11108b3983453f7240522ad7ae895d111037bfa43575e1f7a2333799


Do you want to 1) encrypt parameters, or 2) submit parameters:
2
Enter encrypted parameters (in hex): 
399958001401aed92f50961e9531e4b6
Welcome, admin!

Here's your encrypted flag:
c2f3047788bc20da616d45d4c42c862d435ccba83fabe664d69107e9d9e1708a838c712b8fa58666338527767ceb8ce534599f3b23c4a7077e9872a3db8635f9

Flag: cs409{fu11_k3y_recovery_ftw_1mpl3m3nt_w1th_c4r3}

"""
# ===== YOUR CODE ABOVE =====

try:
    target.close()
except:
    pass
