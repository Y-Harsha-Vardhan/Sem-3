from pwn import *

HOST = "0.cloud.chals.io"
PORT = 32320

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


# ===== YOUR CODE BELOW =====


payload = "00" * 2048  # 2048 zero-bytes
# ===== YOUR CODE ABOVE =====


recvuntil("string: ")
sendline(payload)

for level in range(100):
    recvuntil("c1: ")
    c1 = recvline().strip()

    recvuntil("c2: ")
    c2 = recvline().strip()
    
    recvuntil("c1 or c2: ")

    # ===== YOUR CODE BELOW =====
    # Write code here to decide whether to send c1 or c2
    # The variable c1 (which is of type str) contains the hex-encoded version of c1 returned by the server
    # The variable c2 (which is of type str) contains the hex-encoded version of c2 returned by the server

    b1 = bytes.fromhex(c1)
    b2 = bytes.fromhex(c2)

    has0_1 = (b'\x00' in b1)
    has0_2 = (b'\x00' in b2)

    # If one contains 0x00 and the other doesn't, choosing the one without 0x00
    if has0_1 and (not has0_2):
        guess = 2
    elif has0_2 and (not has0_1):
        guess = 1
    else:
        guess = 1

    # ===== YOUR CODE ABOVE =====

    sendline(f"c{guess}")

recvall()
target.close()
