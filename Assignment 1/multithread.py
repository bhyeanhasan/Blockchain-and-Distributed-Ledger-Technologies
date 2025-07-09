import hashlib
import time
import os
from multiprocessing import Process, Event, Queue, cpu_count

def worker(file_data, algorithm_func, prefix, start_nonce, end_nonce, found_event, result_queue):
    for nonce in range(start_nonce, end_nonce):
        if found_event.is_set():
            return
        hasher = algorithm_func()
        hasher.update(file_data + str(nonce).encode())
        hash_value = hasher.hexdigest()
        if hash_value.startswith(prefix):
            found_event.set()
            result_queue.put((nonce, hash_value))
            return

def find_nonce(file_path, algorithm_name, prefix='0001', chunk_size=10000, max_nonce=10**9):
    hash_algorithms = {
        'MD5': hashlib.md5,
        'SHA1': hashlib.sha1,
        'SHA256': hashlib.sha256,
        'SHA512': hashlib.sha512,
        'SHA3_256': hashlib.sha3_256,
        'SHA3_512': hashlib.sha3_512
    }
    if algorithm_name not in hash_algorithms:
        raise ValueError(f"Unsupported algorithm: {algorithm_name}")

    algorithm_func = hash_algorithms[algorithm_name]

    with open(file_path, 'rb') as f:
        file_data = f.read()

    found_event = Event()
    result_queue = Queue()

    num_processes = cpu_count()
    start_time = time.time()

    current_start = 0
    while current_start < max_nonce and not found_event.is_set():
        processes = []
        for i in range(num_processes):
            start_nonce = current_start + i * chunk_size
            end_nonce = min(start_nonce + chunk_size, max_nonce)
            if start_nonce >= max_nonce:
                break
            print(f"Starting process for nonce range: {start_nonce} to {end_nonce - 1}")
            p = Process(target=worker, args=(
                file_data, algorithm_func, prefix, start_nonce, end_nonce, found_event, result_queue))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        current_start += num_processes * chunk_size

    if result_queue.empty():
        return None, None, time.time() - start_time

    nonce, hash_val = result_queue.get()
    duration = time.time() - start_time
    return nonce, hash_val, duration

def main():
    file_path = "../data/100mb.txt"  # Change to your path
    algorithm_name = 'SHA256'            # Change to 'MD5' or your desired algo
    prefix = '0001'                  # Must match your previous prefix
    chunk_size = 1000
    max_nonce = 10**8

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Starting nonce search with {algorithm_name} and prefix '{prefix}'...")
    nonce, hash_val, duration = find_nonce(file_path, algorithm_name, prefix, chunk_size, max_nonce)

    if nonce is None:
        print(f"No valid nonce found up to {max_nonce}")
    else:
        print(f"✅ Nonce found: {nonce}")
        print(f"Hash: {hash_val}")
        print(f"Time taken: {duration:.4f} seconds")

if __name__ == "__main__":
    main()
