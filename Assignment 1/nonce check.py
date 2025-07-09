file_path = "../data/500mb.txt"

with open(file_path, 'rb') as f:
    file_data = f.read()

nonce = 395330  # or 23370
nonce_bytes = str(nonce).encode()

import hashlib

# For MD5
h = hashlib.sha1()
h.update(file_data + nonce_bytes)
print(h.hexdigest())  # should start with prefix '0001'
