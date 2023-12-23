import time

def print_numbers():
    for i in range(5):
        time.sleep(1) 
        print(f"Thread 1: {i}\n")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)  
        print(f"Thread 2: {letter}\n")

def print_symbols():
    for symbol in '@#$%^@':
        time.sleep(2) 
        print(f"Thread 3: {symbol}\n")

start_time = time.time()

print_numbers()
print_letters()
print_symbols()

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
