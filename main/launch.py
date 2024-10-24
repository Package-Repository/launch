from multiprocessing                import Process, Value
from kill_button_interface          import Kill_Button_Interface
from main.shared_memory                  import SharedMemoryWrapper
from PID_controller.pid_interface   import PIDInterface
from sensors.a50_dvl.dvl_interface  import DVL_Interface

"""
    discord: @kialli
    github: @kchan5071
    
    This is the main file that will be run to start the program.
    Combined the old launch.py with the launch.py.DVL_Test
    
"""
def main():

    # create shared memory
    shared_memory_object = SharedMemoryWrapper()

    # create objects
    PID_interface = PIDInterface(shared_memory_object)
    dvl_object = DVL_Interface(shared_memory_object)
    
    #create processes
    PID_process = Process(target=PID_interface.run_loop)
    dvl_process = Process(target=dvl_object.run_loop)

    # start processes
    PID_process.start()
    dvl_process.start()

    # wait for processes to finish
    PID_process.join()
    dvl_process.join()

    #END
    print("Program has finished")

if __name__ == '__main__':
    print("RUN FROM LAUNCH")
    main()