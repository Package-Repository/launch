from multiprocessing import Process, Value
from subprocess import call

class Example_Process:
    def __init__(self, shared_memory_object):
        self.shared_memory_object = shared_memory_object


    def run_loop(self):
        while self.shared_memory_object.running.value:
            #write code here


            #end
            pass
