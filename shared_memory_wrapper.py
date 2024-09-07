from multiprocessing import Value, Array


class SharedMemoryWrapper:
    def __init__(self):
        #add properties here
        self.example_array          = Array('i', [1, 2, 3, 4, 5])
        self.running                = Value('i', 1)