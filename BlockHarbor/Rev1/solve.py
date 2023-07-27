import ctypes
MAX_SIZE = 32

a = 1103515245
c = 12345
m = 2147483647
seed = 1337

user_input = bytearray(MAX_SIZE)
STATE = [0x1e48add6, 0xaaa7550c, 0x18df53bf, 0xe6af1116]

start = [0x0, 0x0, 0x0, 0x0]
def uint32(num):
    return ctypes.c_uint32(num).value   

def gen_random():
    global seed
    seed = ((a * seed + c) % m)
    return seed

def check_pass(start):
    print("checking")
    for i in range(4):
        temp = start[i]
        temp *= 0xcafebeef
        a=gen_random()
        print(a)
        temp += a    #78629421
        temp *= 0xfacefeed
        a=gen_random()
        print(a)
        temp ^= a    #1554612952         648428601
        print(uint32(temp))
        if uint32(temp) != STATE[i]:
            return False
    return True

def setup():
    print("==================================================")
    print("=               SECURE LOCK - v0.5               =")
    print("==================================================")

def loop():
    global start

    user_input = bytearray(MAX_SIZE)
    start = [0x0, 0x0, 0x0, 0x0]

    print("Enter your password: ")
    user_input = bytearray(input().encode())
    for i in range(4):
        start[i] |= (user_input[i * 4] << 24)    
        print(user_input[i * 4])
        start[i] |= (user_input[i * 4 + 1] << 16)
        start[i] |= (user_input[i * 4 + 2] << 8)
        start[i] |= (user_input[i * 4 + 3])

    if check_pass(start):
        print("Thats it!\r\nSubmit in the format FLAG{", end="")
        for i in range(4):
            print(format(start[i], 'X'), end="")
        print("}")
        while True:
            pass
    else:
        print("Incorrect password!")
        while True:
            pass

if __name__ == "__main__":
    setup()
    loop()

