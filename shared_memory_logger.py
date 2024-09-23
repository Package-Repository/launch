from multiprocessing import Value, Array
from multiprocessing.sharedctypes import SynchronizedArray
from shared_memory_wrapper import SharedMemoryWrapper
import time

class SharedMemoryLogger:
    def __init__(self, shared_memory_wrapper):
        self.shared_memory_wrapper = shared_memory_wrapper
        self.file_name = 'log'

    def run_loop(self):
        file = open(self.file_name, 'w')
        while self.shared_memory_wrapper.running.value:
            time.sleep(5)
            print("Logging")
            file.write(time.ctime() + "\n")
            vars = self.shared_memory_wrapper.__dict__
            self.save(vars, file)
    
    def save(self, vars, file):
        for var in vars:
            if type(vars[var]) != SynchronizedArray:
                file.write(f"{var}: {vars[var].value}\n")
            else:
                file.write(f"{var}: {vars[var][:]}\n")

        file.write("\n")
        
