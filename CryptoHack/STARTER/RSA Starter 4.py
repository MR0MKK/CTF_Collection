from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

e = 65537

phi = (p - 1) * (q - 1)
d = pow(e,-1,phi)

print(d)