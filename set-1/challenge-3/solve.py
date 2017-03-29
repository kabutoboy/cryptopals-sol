from itertools import zip_longest
from binascii import a2b_hex
from binascii import b2a_hex
from operator import itemgetter

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstwxyz0123456789 +-*/='
xor = {}
xor_inv = {}

for a in alphabet:
    zipped = zip_longest(a, alphabet, fillvalue=a)
    for p in list(zipped):
        o0, o1 = ord(p[0]), ord(p[1])
        res = ((o0 & ~o1) | (~o0 & o1)) & 0xff
        #    .to_bytes(1, byteorder='big', signed=True)
        xor[p] = 0
        xor_inv.setdefault(res, []).append(p)

#print(xor_inv)

hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
bin = a2b_hex(hex)

print(bin)

for b in bin:
    for p in xor_inv[b]:
        xor[p] += 1
    #print(xor_inv[b])

for k in max(xor, key=xor.get):
    ans = b''
    for b in bin:
        ans += ((ord(k) & ~b) | (~ord(k) & b)).to_bytes(1, byteorder='big', signed=True)
    print('key is', k, 'ans is', b2a_hex(ans))
