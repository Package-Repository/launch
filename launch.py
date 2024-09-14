from multiprocessing                import Process, Value
from kill_button_interface          import Kill_Button_Interface
from shared_memory                  import SharedMemoryWrapper
from PID_controller.pid_interface   import PIDInterface

"""
    discord: @kialli
    github: @kchan5071
    
    This is the main file that will be run to start the program.
    
"""
def main():

    # create shared memory
    shared_memory_object = SharedMemoryWrapper()
    shared_memory_object.target_x.value = 13
    shared_memory_object.target_y.value = -20
    shared_memory_object.target_z.value = -10

    # create objects
    PID_interface = PIDInterface(shared_memory_object)

    #create processes
    PID_process = Process(target=PID_interface.run_loop)
    
    # start processes
    PID_process.start()

    # wait for processes to finish
    PID_process.join()


    #END
    print("Program has finished")

if __name__ == '__main__':
    print("RUN FROM LAUNCH")
    main()