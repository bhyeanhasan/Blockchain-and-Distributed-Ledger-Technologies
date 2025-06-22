import hashlib
import time

files = [
    "../data/100MB.txt",
    "../data/50MB.txt"
]

# Student ID : 1024312001

prefix = "000001"


def hash_md5(file_path):
    md5 = hashlib.md5()
    start = time.time()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    end = time.time()
    hash_value = prefix + md5.hexdigest()
    print(f"MD5 -> Hash: {hash_value} || Time: {end - start:.4f}s")


def hash_sha1(file_path):
    sha1 = hashlib.sha1()
    start = time.time()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    end = time.time()
    hash_value = prefix + sha1.hexdigest()
    print(f"SHA-1 -> Hash: {hash_value} || Time: {end - start:.4f}s")


def hash_sha256(file_path):
    sha256 = hashlib.sha256()
    start = time.time()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    end = time.time()
    hash_value = prefix + sha256.hexdigest()
    print(f"SHA-256 -> Hash: {hash_value} || Time: {end - start:.4f}s")


def hash_sha512(file_path):
    sha512 = hashlib.sha512()
    start = time.time()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha512.update(chunk)
    end = time.time()
    hash_value = prefix + sha512.hexdigest()
    print(f"SHA-512 -> Hash: {hash_value} || Time: {end - start:.4f}s")


def hash_sha3_256(file_path):
    sha3_256 = hashlib.sha3_256()
    start = time.time()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha3_256.update(chunk)
    end = time.time()
    hash_value = prefix + sha3_256.hexdigest()
    print(f"SHA3-256 -> Hash: {hash_value} || Time: {end - start:.4f}s")


def hash_sha3_512(file_path):
    sha3_512 = hashlib.sha3_512()
    start = time.time()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha3_512.update(chunk)
    end = time.time()
    hash_value = prefix + sha3_512.hexdigest()
    print(f"SHA3-512 -> Hash: {hash_value} || Time: {end - start:.4f}s")


for file in files:
    print("File: ", file)
    hash_md5(file)
    hash_sha1(file)
    hash_sha256(file)
    hash_sha512(file)
    hash_sha3_256(file)
    hash_sha3_512(file)
    print("\n")
