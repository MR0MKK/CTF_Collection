def xor_strings(a, b):
    return "".join(chr(ord(x) ^ 104) for x in map(chr.__xor__, map(ord, a), map(ord, b)))

def mess(a):
    return "".join(a[i] for i in range(len(a)) if i % 2 == 0), "".join(a[i] for i in range(len(a)) if i % 2 == 1)

def encrypt(message):
    a, b = mess(list(map(lambda x: str(ord(x)), message)))
    return xor_strings(a, b)

if __name__ == "__main__":
    result = encrypt("ictf{REDACTED}")
    expected_result = "f-Yefl*Y+E:Y.Y-.uncs#E~fa/npA?e/H;rKlg"
    print(result == expected_result)
