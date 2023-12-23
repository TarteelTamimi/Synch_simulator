>Tarteel Tamimi - 211129
# Step-by-step how I build this project:
-------------------------
## 👉 FIRST -> *Find the difference between regular programming and thread programming by simple tasks and without shared variables.*
I created two files in my project folder, the first one is `withoutTreads.py` and the second one is `withTreads.py`, in order to compare the time each one will take -to observe the effectiveness of Threads in programming- .


I wrote three functions in the first file, each one do a particular task, I use the `time.sleep()` to simulate some work that takes time, and use this code:

```python
start_time = time.time()
#my code
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
```

to calculate exactly how much time each method takes , and then I called the functions.

#### ✨ I noteced that the file which has 3 threads completed all tasks 10 seconds faster than the file without threads, whitch is a long time ✨

```python
#copy of withoutTreads.py file

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
```
```python
#copy of withTreads.py file

import threading
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

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=print_symbols)

start_time = time.time()
# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
thread3.join()

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
```
--------------------------

## 👉 SECOND -> *Thread programming with shared variable*
I created a global variable named `counter` as a shared variable with initial value 1000. And I use `Lock()` class, so an instance of the lock can be created and then acquired by threads before accessing a critical section, and released after the critical section -ensuring thread safety-.
I define two functions, producer and consumer.

```python
#copy of withTreads.py file

import threading

counter = 1000

lock = threading.Lock()

def producer():
    global counter
    
    lock.acquire()
    try:
        counter += 1    
    finally:
        lock.release()

def consumer():
    global counter

    lock.acquire()
    try:
        counter -= 1    
    finally:
        lock.release()

# Create two threads
thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(f"The value of the counter is {counter}")
```
-------------------------------

## 👉 THIRED -> *Generate a random number of threads*
In this step I define a function that generate more than one thread and put them in an array, then start it one-by-one, this code will output a list of all the threads worked, with its number and what it does (increase/decrease the counter), in the end it prints the final value of the counter.

```python
#copy of withTreads.py file

import threading
import random

counter = 1000
print(f'The initial value of the counter is: {counter}')

lock = threading.Lock()

#to increase the counter by 1
def producer(thread_id):
    global counter

    with lock:
        while counter >= 1800:
            pass
        counter += 1

    print(f'Thread {thread_id}: counter++.')   


#to decrease the counter by 1
def consumer(thread_id):
    global counter

    with lock:
        while counter <= 0:
            pass
        counter -= 1

    print(f'Thread {thread_id}: counter--.')  


#to Choose one random thread from all created threads to work on 
def generate_unique_random_numbers(num_threads):
    unique_numbers = random.sample(range(1, num_threads+1), num_threads)
    return unique_numbers


#to create a rendom number of threads and use it   
def create_random_threads():
    num_threads = random.randint(1, 10)
    
    threads = []
    for i in generate_unique_random_numbers(num_threads):
        if i % 2 == 0:
            thread = threading.Thread(target=producer, args=(i,))
        else:
            thread = threading.Thread(target=consumer, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


create_random_threads()
print(f'The final value of the counter is: {counter}')
```
