from multiprocessing                import Process, Value
from shared_memory_wrapper          import SharedMemoryWrapper
from sensors.a50_dvl.dvl_interface  import DVL_Interface
from shared_memory_logger           import SharedMemoryLogger
from kill_button                    import KillButtonInterface
import cherrypy
from ui_webserver                   import LiveUpdateUIServer

"""
    discord: @kialli
    github: @kchan5071
    
    This is the main file that will be run to start the program.
    
"""
def main():

    # create shared memory
    shared_memory_object = SharedMemoryWrapper()

    # create objects
    logger_object = SharedMemoryLogger(shared_memory_object)
    # dvl_object = DVL_Interface(shared_memory_object)

    #ADD OBJECTS HERE   

    #create processes
    logger_object_process = Process(target=logger_object.run_loop)
    # dvl_process = Process(target=dvl_object.run_loop)

    #ADD PROCESSES HERE
    
    # start processes
    logger_object_process.start()
    # dvl_process.start()
    cherrypy.quickstart(LiveUpdateUIServer(shared_memory_object))

    #ADD START PROCESSES HERE

    # wait for processes to finish
    logger_object_process.join()
    # dvl_process.join()

    #ADD JOIN PROCESSES HERE



    #END
    print("Program has finished")

if __name__ == '__main__':
    print("RUN FROM LAUNCH")
    main()
