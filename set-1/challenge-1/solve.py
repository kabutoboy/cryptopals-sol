from binascii import a2b_hex
from base64 import b64encode

h = input()
b = a2b_hex(h)
encoded = b64encode(b)
print(encoded)
