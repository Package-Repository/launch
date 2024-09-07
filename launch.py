from multiprocessing                import Process, Value
from example_process                import Example_Process
from kill_button_interface          import Kill_Button_Interface
from shared_memory_wrapper          import SharedMemoryWrapper

"""
    discord: @kialli
    github: @kchan5071
    
    This is the main file that will be run to start the program.
    
"""
def main():

    # create shared memory
    shared_memory_object = SharedMemoryWrapper()

    # create objects
    kill_button_listener = Kill_Button_Interface(running = shared_memory_object.running)
    example_object = Example_Process(shared_memory_object) 

    #ADD OBJECTS HERE   

    #create processes
    kill_button_listener_process = Process(target=kill_button_listener.run_loop)
    example_process = Process(target=example_object.run_loop)

    #ADD PROCESSES HERE
    
    # start processes
    kill_button_listener_process.start()
    example_process.start()

    #ADD START PROCESSES HERE

    # wait for processes to finish
    kill_button_listener_process.join()
    example_process.join()

    #ADD JOIN PROCESSES HERE



    #END
    print("Program has finished")

if __name__ == '__main__':
    print("RUN FROM LAUNCH")
    main()
