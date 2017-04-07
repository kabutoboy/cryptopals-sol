from itertools import chain

C = bytearray.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
for k in chain(range(ord('a'), ord('z')), range(ord('A'), ord('Z'))):
    M = bytearray(map(lambda c: c ^ k, C))
    print(chr(k), M.decode())
