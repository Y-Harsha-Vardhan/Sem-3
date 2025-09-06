from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

HOST = "0.cloud.chals.io"
PORT = 23369

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


def send_to_server(input: str) -> tuple[str, str]:
    recvuntil("$ ")
    sendline(input)
    recvuntil("Encrypted Input (hex): ")
    inp_enc = recvline().strip()
    recvuntil("Encrypted Output (hex): ")
    outp_enc = recvline().strip()
    return (inp_enc, outp_enc)


# ===== YOUR CODE BELOW =====
# Use the send_to_server(input) function to send your input (str) to the server
# It returns a 2-tuple of strings as output: the first component being the encrypted input (hex-string), the second component being the encrypted output (hex-string)

# We know that in CTR Mode, C = P ^ KS (where KS is the Key Stream)
# If the server reuses KS for two encryptions, then P1 ^ C1 = KS and P2 = C2 ^ KS
# So, first we will send a known P1 and get C1 -> using these two we can compute KS = P1 ^ C1
# Then we can request the encrypted flag Cflag, and compute Pflag = Cflag ^ KS
# The following code exploits this idea to retrieve the flag:

##############################################################################################
n = AES.block_size

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

# We need to choose a known plaintext which is long enough to recover the keystream
# Let the known flag length be l, we need to choose plaintext length greater than this
# Lets first try 2048 bytes
l = 2048
known_plaintext = b'A' * l

# Sending this known plaintext to the server:
enc_inp_HEX, enc_out_HEX = send_to_server(known_plaintext.decode())
enc_inp = bytes.fromhex(enc_inp_HEX)

# Now using the enc_inp and enc_out, we can find the keystream = enc_inp ^ known_plaintext
ks = xor_bytes(enc_inp, known_plaintext)

# Now we can request the encryped flag by the command: !flag
enc_flag_in_HEX, enc_flag_out_HEX = send_to_server("!flag")
flag_cipher = bytes.fromhex(enc_flag_out_HEX)

# Now we just need to decrypt the flag by XORing it with the keystream
# Actually, for l = 1024, it didn't work so I then made it l = 2048
if len(ks) < len(flag_cipher):
    print ("The length l is small")
else:
    for shift in range(len(ks) - len(flag_cipher)):
        XOR_text = xor_bytes(flag_cipher, ks[shift:shift+len(flag_cipher)])
        try: 
            text = XOR_text.decode()
        except UnicodeDecodeError:
            text = XOR_text.decode(errors="ignore")

        if "cs409{" in text:
            print(f"Flag: {text}")
            break
# We get the flag: cs409{y0u_kn0w_th3_gr34t35t_f1lm5_of_4ll_t1m3_w3re_n3v3r_m4d3}
##############################################################################################
# ===== YOUR CODE ABOVE =====

target.close()
