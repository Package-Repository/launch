from multiprocessing import Process, Value, set_start_method
from vision.vision.vision_main import VideoRunner
from shared_memory_reader import SharedMemoryReader
#"/vision/vision/vision_main.py"
def main():
    # try:
    #     set_start_method('spawn')
    # except RuntimeError:
    #     pass
    
    #create shared memory
    ang_vel_x = Value('d', 0.0)
    ang_vel_y = Value('d', 0.0)
    ang_vel_z = Value('d', 0.0)
    lin_acc_x = Value('d', 0.0)
    lin_acc_y = Value('d', 0.0)
    lin_acc_z = Value('d', 0.0)
    orientation_x = Value('d', 0.0)
    orientation_y = Value('d', 0.0)
    orientation_z = Value('d', 0.0)
    depth = Value('d', 0.0)
    offset_x = Value('d', 0.0)
    offset_y = Value('d', 0.0)
    
    
    vis = VideoRunner(linear_acceleration_x=lin_acc_x, linear_acceleration_y=lin_acc_y, linear_acceleration_z=lin_acc_z,        #linear accel x y z
                        angular_velocity_x=ang_vel_x, angular_velocity_y=ang_vel_y, angular_velocity_z=ang_vel_z,               #angular velocity x y z
                        orientation_x=orientation_x, orientation_y=orientation_y, orientation_z=orientation_z,                  #orientation x y z
                        depth=depth,                                                                                            #depth
                        offset_x=offset_x, offset_y=offset_y)                                                                   #offset x y
    
    shm = SharedMemoryReader(linear_acceleration_x=lin_acc_x, linear_acceleration_y=lin_acc_y, linear_acceleration_z=lin_acc_z, #linear accel x y z
                        angular_velocity_x=ang_vel_x, angular_velocity_y=ang_vel_y, angular_velocity_z=ang_vel_z,               #angular velocity x y z
                        orientation_x=orientation_x, orientation_y=orientation_y, orientation_z=orientation_z,                  #orientation x y z                 
                        depth=depth,                                                                                            #depth
                        offset_x=offset_x, offset_y=offset_y)                                                                   #offset x y
    
    #create processes
    zed_process = Process(target=vis.run_loop)
    reader_process = Process(target=shm.run_loop)
    
    # start processes
    zed_process.start()
    reader_process.start()
    
    # join processes
    zed_process.join()
    reader_process.join()
    

if __name__ == '__main__':
    main()