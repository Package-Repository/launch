from multiprocessing                        import Process, Value
from shared_memory                          import SharedMemoryWrapper
from utils.kill_button_interface            import Kill_Button_Interface
from modules.motors.MotorInterface          import MotorInterface
#from modules.pid.pid_interface              import PIDInterface
#from modules.sensors.a50_dvl.dvl_interface  import DVL_Interface
from modules.vision.vision_main             import VideoRunner

"""
    discord: @kialli
    github: @kchan5071
    
    This is the main file that will be run to start the program.
    Combined the old launch.py with the launch.py.DVL_Test
    
"""
def main():
    temp_x_hard_deadzone = 400 #FIXME

    # create shared memory
    shared_memory_object = SharedMemoryWrapper()

    # create objects
    #PID_interface = PIDInterface(shared_memory_object)
    #dvl_object = DVL_Interface(shared_memory_object)
    vis_object = VideoRunner(shared_memory_object, temp_x_hard_deadzone) #, shared_memory_object.x_hard_deadzone)
    kill_btn = Kill_Button_Interface(shared_memory_object)
    interface = MotorInterface(shared_memory_object)
    
    
    #create processes
    #PID_process = Process(target=PID_interface.run_loop)
    #dvl_process = Process(target=dvl_object.run_loop)
    vis_process = Process(target=vis_object.run_loop)
    kill_btn_process = Process(target=kill_btn.run_loop)
    interface_process = Process(target=interface.run_loop)

    # start processes
    #PID_process.start()
    #dvl_process.start()
    vis_process.start()
    kill_btn_process.start()
    interface_process.start()

    # wait for processes to finish
    #PID_process.join()
    #dvl_process.join()
    vis_process.join()
    kill_btn_process.join()
    interface_process.join()

    #END
    print("Program has finished")

if __name__ == '__main__':
    print("RUN FROM LAUNCH")
    main()