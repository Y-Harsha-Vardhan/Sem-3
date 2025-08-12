import hashlib

def group_sub(m1: bytes, m2: bytes) -> bytes:
    assert len(m1) == len(m2)
    res = b""
    for i in range(len(m1)):
        res += chr((m2[i] - m1[i]) % 128).encode()
    return res

def generate_key(start_byte: int, length: int) -> bytes:
    key = chr(start_byte).encode()
    for _ in range(1, length):
        key += chr(hashlib.sha256(key).digest()[0] % 128).encode()
    return key

with open("ciphertext.enc", "rb") as f:
    ciphertext = f.read()

# A brute force which checks all possible 128 combinations of the key (because it can be generated using the first byte)
# Then comparing it with the flag format, which must contain { and }
for start_byte in range(128):
    key = generate_key(start_byte, len(ciphertext))
    plaintext = group_sub(key, ciphertext)
    if b"{" in plaintext and b"}" in plaintext:  # Bruteforce check for flag format
        print(f"[+] Found plausible flag with start byte {start_byte}: {plaintext}")

# This way, we get the most plausible flag is: cs409{algebra_enters_the_picture!}