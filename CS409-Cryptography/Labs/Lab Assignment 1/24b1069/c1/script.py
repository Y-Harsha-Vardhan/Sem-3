from Crypto.Util.strxor import strxor
from Crypto.Random import get_random_bytes

with open("ciphertext1.enc", "rb") as f:
    Cipher_Flag = f.read()

with open("ciphertext2.enc", "rb") as f:
    Cipher_Message = f.read()

# When we apply strxor to the two given cipher texts, we get M1(Flag) XOR M2(MSG)
M1_XOR_M2 = strxor(Cipher_Flag, Cipher_Message)

# These are some helper functions that will help guess the message and flag:
def Helper(a):
    n = len(a)
    extra = b"0"*(l - n)
    var = a + extra
    print(strxor(var, M1_XOR_M2)[0:n])

# We are also given that the flag starts with cs409{ and that the MSG is just a normal English sentence
# So, lets first use this information to find the first 6 letters of M1_XOR_M2
# We also know that the length of M1_XOR_M2 is 53 using len() function
# Here we are going to strxor the M1_XOR_M2 with the known string in the flag ("cs409{")
l = 53 # This is the length of the flag and message
flag = b"cs409{" 
n = len(flag) # This is the number of characters of the flag, that we know
extra = b"0"*(l - n)
flag = flag + extra
print(strxor(flag, M1_XOR_M2)[0:n])

# Here we get that the first 6 characters of the MSG are: Crypta
# The possible words relevant are: Cryptanalysis, Cryptanalytic, Cryptanalyst
# So, lets assume that the first few characters of the message are: "Cryptanalysis "
message = b"Crypta" + b"nalysis " 
n = len(message)
extra = b"0"*(l - n)
message = message + extra
print(strxor(M1_XOR_M2, message)[0:n])

# Here we get that the first few characters of the flag are: "cs409{one_time_pad"
flag = b"cs409{one_time_pad"
Helper(flag)

# Now we get that the first few characters of the message are: "Cryptanalysis frequently"
message = b"Cryptanalysis frequently "
Helper(message)

# Flag: "cs409{one_time_pad_key_reuse_"
flag = b"cs409{one_time_pad_key_reuse_"
Helper(flag)

# Message: "Cryptanalysis frequently involves"
message = b"Cryptanalysis frequently involves "
Helper(message)

# Flag: "cs409{one_time_pad_key_reuse_compromises_security_"
flag = b"cs409{one_time_pad_key_reuse_compromises_security"
Helper(flag)

# Message: "Cryptanalysis frequently involves statistical attack "
message = b"Cryptanalysis frequently involves statistical attack"
Helper(message)

# Flag: "cs409{one_time_pad_key_reuse_compromises_security!!!}"
flag = b"cs409{one_time_pad_key_reuse_compromises_security!!!}"
Helper(flag)

# Message: "Cryptanalysis frequently involves statistical attacks"