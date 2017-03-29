from binascii import a2b_hex
from binascii import b2a_hex

h1 = '1c0111001f010100061a024b53535009181c'
h2 = '686974207468652062756c6c277320657965'

b1 = a2b_hex(h1)
b2 = a2b_hex(h2)

b3 = b''
zipped = zip(b1, b2)
for pair in list(zipped):
    b = (pair[0] & ~pair[1]) | (~pair[0] & pair[1])
    b3 += b.to_bytes(1, byteorder='big', signed=True)

res = b2a_hex(b3)
print(res)
