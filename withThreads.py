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
