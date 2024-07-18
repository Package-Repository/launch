from multiprocessing                import Process, Value
from vision.vision_main             import VideoRunner
from shared_memory_reader           import SharedMemoryReader
from sensors.depth_sensor_interface import DepthSensorInterface
from motors.MotorInterface          import MotorInterface

'''
    discord: @kialli
    github: @kchan5071
    
    creates shared memory and processes to communicate between vision and control
    
    vision: writes to shared memory
    currently just printing process data, later to use with PID control
    
    could use arrays, too lazy
    
'''

def main():
    ang_vel_x                   = Value('d', 0.0)
    ang_vel_y                   = Value('d', 0.0)
    ang_vel_z                   = Value('d', 0.0)
    lin_acc_x                   = Value('d', 0.0)
    lin_acc_y                   = Value('d', 0.0)
    lin_acc_z                   = Value('d', 0.0)
    orientation_x               = Value('d', 0.0)
    orientation_y               = Value('d', 0.0)
    orientation_z               = Value('d', 0.0)
    depth                       = Value('d', 0.0)
    offset_x                    = Value('d', 0.0)
    offset_y                    = Value('d', 0.0)
    depth_z                     = Value('d', 0.0)    
    
    depth_sensor = DepthSensorInterface(z=depth_z)
    
    vis = VideoRunner(
        linear_acceleration_x   = lin_acc_x,
        linear_acceleration_y   = lin_acc_y,
        linear_acceleration_z   = lin_acc_z,
        angular_velocity_x      = ang_vel_x,
        angular_velocity_y      = ang_vel_y,
        angular_velocity_z      = ang_vel_z,
        orientation_x           = orientation_x,
        orientation_y           = orientation_y,
        orientation_z           = orientation_z,
        depth                   = depth,
        offset_x                = offset_x,
        offset_y                = offset_y
    )

    interface = MotorInterface(
        linear_acceleration_x   = lin_acc_x,
        linear_acceleration_y   = lin_acc_y,
        linear_acceleration_z   = lin_acc_z,
        angular_velocity_x      = ang_vel_x,
        angular_velocity_y      = ang_vel_y,
        angular_velocity_z      = ang_vel_z,
        orientation_x           = orientation_x,
        orientation_y           = orientation_y,
        orientation_z           = orientation_z,
        depth                   = depth,
        offset_x                = offset_x,
        offset_y                = offset_y,
        dvl_z                   = depth_z
    )       
    
    shm = SharedMemoryReader(
        linear_acceleration_x   = lin_acc_x,
        linear_acceleration_y   = lin_acc_y,
        linear_acceleration_z   = lin_acc_z,
        angular_velocity_x      = ang_vel_x,
        angular_velocity_y      = ang_vel_y,
        angular_velocity_z      = ang_vel_z,
        orientation_x           = orientation_x,
        orientation_y           = orientation_y,
        orientation_z           = orientation_z,             
        depth                   = depth,
        offset_x                = offset_x,
        offset_y                = offset_y
    )
    
    #create processes
    zed_process                 = Process(target=vis.run_loop)
    reader_process              = Process(target=shm.run_loop)
    depth_sensor_process        = Process(target=depth_sensor.run_loop)
    interface                   = Process(target=interface.run_loop)
    
    # start processes
    zed_process.start()
    reader_process.start()
    depth_sensor.start()
    interface.start()
    
    # join processes
    zed_process.join()
    reader_process.join()
    depth_sensor.join()
    interface.join()
    

if __name__ == '__main__':
    main()
