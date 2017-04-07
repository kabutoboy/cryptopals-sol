from base64 import b64encode

h = input()
b = bytes.fromhex(h)
encoded = b64encode(b)
print(encoded)
