import hashlib
import time
import os

# Define the hash algorithms
hash_algorithms = {
    'MD5': hashlib.md5,
    'SHA1': hashlib.sha1,
    'SHA256': hashlib.sha256,
    'SHA512': hashlib.sha512,
    'SHA3_256': hashlib.sha3_256,
    'SHA3_512': hashlib.sha3_512
}

# Function to find nonce such that hash starts with the given prefix
def find_nonce(file_path, algorithm_func, prefix='000', buffer_size=65536):
    nonce = 0
    start_time = time.time()
    with open(file_path, 'rb') as f:
        file_data = f.read()
    while True:
        hasher = algorithm_func()
        hasher.update(file_data + str(nonce).encode())
        hash_value = hasher.hexdigest()
        if hash_value.startswith(prefix):
            break
        nonce += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    return nonce, hash_value, elapsed_time

# Main function to process files
def main():
    file_paths = [    "../data/100mb.txt",
    "../data/500mb.txt",
    "../data/1000mb.txt"]  # Replace with actual paths
    prefix = '0001'  # Desired hash prefix

    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        print(f"\nProcessing file: {file_path}")
        for algo_name, algo_func in hash_algorithms.items():
            nonce, hash_val, duration = find_nonce(file_path, algo_func, prefix)
            print(f"{algo_name}:\n  Nonce: {nonce}\n  Hash: {hash_val}\n  Time: {duration:.4f} seconds")

if __name__ == "__main__":
    main()
