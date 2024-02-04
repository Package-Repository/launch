from multiprocessing import Process, Queue

def producer(queue):
    # Enqueue arrays of three strings
    queue.put(["string1", "string2", "string3"])
    queue.put(["string4", "string5", "string6"])
    queue.put(["string7", "string8", "string9"])

def consumer(queue):
    # Dequeue and print the arrays
    while not queue.empty():
        array = queue.get()
        print(array)

if __name__ == "__main__":
    # Create a shared queue
    queue = Queue()

    # Create and start the producer process
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()

    # Create and start the consumer process
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()

    # Wait for the producer process to finish
    producer_process.join()

    # Wait for the consumer process to finish
    consumer_process.join()
