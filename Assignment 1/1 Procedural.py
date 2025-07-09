import hashlib
import time
import os
import multiprocessing as mp

# Define the hash algorithms
hash_algorithms = {
    'MD5': hashlib.md5,
    'SHA1': hashlib.sha1,
    'SHA256': hashlib.sha256,
    'SHA512': hashlib.sha512,
    'SHA3_256': hashlib.sha3_256,
    'SHA3_512': hashlib.sha3_512
}

# Worker function for multiprocessing
def hash_worker(start_nonce, step, file_data, prefix, algorithm_name):
    algo_func = hash_algorithms[algorithm_name]
    nonce = start_nonce
    while True:
        hasher = algo_func()
        hasher.update(file_data + str(nonce).encode())
        hash_val = hasher.hexdigest()
        if hash_val.startswith(prefix):
            return nonce, hash_val
        nonce += step

# Function to find nonce in parallel
def find_nonce_parallel(file_path, algorithm_name, prefix='0001'):
    start_time = time.time()
    with open(file_path, 'rb') as f:
        file_data = f.read()

    cpu_count = mp.cpu_count()
    with mp.Pool(processes=cpu_count) as pool:
        results = [
            pool.apply_async(hash_worker, args=(i, cpu_count, file_data, prefix, algorithm_name))
            for i in range(cpu_count)
        ]
        # Wait for first successful result
        for res in results:
            try:
                nonce, hash_val = res.get(timeout=300)  # 5-minute max timeout per process
                end_time = time.time()
                return nonce, hash_val, end_time - start_time
            except mp.TimeoutError:
                continue

    return None, None, None  # If not found within timeout

# Main function to process files
def main():
    file_paths = [
        "../data/100mb.txt",
        "../data/500mb.txt",
        "../data/1000mb.txt"
    ]
    prefix = '0001'

    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        print(f"\nProcessing file: {file_path}")
        for algo_name in hash_algorithms.keys():
            nonce, hash_val, duration = find_nonce_parallel(file_path, algo_name, prefix)
            if nonce is not None:
                print(f"{algo_name}:\n  Nonce: {nonce}\n  Hash: {hash_val}\n  Time: {duration:.2f} seconds")
            else:
                print(f"{algo_name}: No valid nonce found within timeout.")

if __name__ == "__main__":
    main()
