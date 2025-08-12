# Converts byte sequence to integer
def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')

# Converts integer x to byte sequence of given length
def int_to_bytes(x, length):
    return x.to_bytes(length, byteorder='big')

# Converts the integer 'number' from base_from to list of digits in base_to
def baseConverter(number, base_from, base_to):
    digits = []
    while number > 0:
        digits.append(number % base_to)
        number //= base_to
    digits.reverse()
    return digits if digits else [0]

def decrypt(ciphertext_bytes, key_bytes):
    # Converting ciphertext bytes (base-256) to integer
    ciphertext_int = bytes_to_int(ciphertext_bytes)

    # Converting ciphertext integer to base-255 digits
    c_digits = baseConverter(ciphertext_int, 256, 255)

    key_digits = list(key_bytes[:len(c_digits)])

    # Decryption: p_i = (c_i - k_i + 1) mod 255
    p_digits = [(c - k + 1) % 255 for c, k in zip(c_digits, key_digits)]

    # Converting decrypted base-255 digits back to integer
    m_int = 0
    for d in p_digits:
        m_int = m_int * 255 + d

    # Converting integer to bytes
    # Length is unknown, but ciphertext length is a good guess
    # Let's try ciphertext length in bytes as flag length
    flag_len = len(ciphertext_bytes)
    flag_bytes = int_to_bytes(m_int, flag_len)

    return flag_bytes

if __name__ == "__main__":
    with open("ciphertext.enc", "rb") as f:
        ciphertext_bytes = f.read()
    with open("keyfile", "rb") as f:
        key_bytes = f.read()

    flag = decrypt(ciphertext_bytes, key_bytes)
    print("Decrypted flag:", flag)
