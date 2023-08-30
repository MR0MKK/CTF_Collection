from Crypto.Util.number import inverse

e = 65537
c = 12
p = 17
q = 23

n = p * q

d = pow(c,e,n)

print(d)