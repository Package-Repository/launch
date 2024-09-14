from multiprocessing                import Process, Value
from vision.vision_main             import VideoRunner
from shared_memory_reader           import SharedMemoryReader
from sensors.depth_sensor_interface import DepthSensorInterface
from motors.MotorInterface          import MotorInterface
from kill_button_interface          import Kill_Button_Interface
from shared_memory                  import SharedMemoryWrapper
import ctypes

import time

"""
    discord: @kialli
    github: @kchan5071
    
    creates shared memory and processes to communicate between vision and control
    
    vision: writes to shared memory
    currently just printing process data, later to use with PID control
    
    could use arrays, too lazy
    
"""
def main():
    # create shared memory
    shared_memory_object = SharedMemoryWrapper()
    X_HARD_DEADZONE             = 400


    depth_sensor = DepthSensorInterface(shared_memory_object)

    kill_button_listener = Kill_Button_Interface(running = shared_memory_object.running)

    vis = VideoRunner(
        shared_memory_object=shared_memory_object,
        hard_deadzone           = X_HARD_DEADZONE
    )

    interface = MotorInterface(shared_memory_object=shared_memory_object,
        x_hard_deadzone         = X_HARD_DEADZONE
    )       

    shm = SharedMemoryReader(
        linear_acceleration_x   = shared_memory_object.imu_lin_acc[0],
        linear_acceleration_y   = shared_memory_object.imu_lin_acc[1],
        linear_acceleration_z   = shared_memory_object.imu_lin_acc[2],
        angular_velocity_x      = shared_memory_object.imu_ang_vel[0],
        angular_velocity_y      = shared_memory_object.imu_ang_vel[1],
        angular_velocity_z      = shared_memory_object.imu_ang_vel[2],
        orientation_x           = shared_memory_object.imu_orientation[0],
        orientation_y           = shared_memory_object.imu_orientation[1],
        orientation_z           = shared_memory_object.imu_orientation[2],
        distance                = shared_memory_object.distance_from_object,
        yolo_offset_x           = shared_memory_object.yolo_offset[0],
        yolo_offset_y           = shared_memory_object.yolo_offset[1],
        color                   = shared_memory_object.current_color_index,
        depth                   = shared_memory_object.depth,
        color_offset_x          = shared_memory_object.color_offset[0],
        color_offset_y          = shared_memory_object.color_offset[1],
        color_enable            = shared_memory_object.color_enable,
        yolo_enable             = shared_memory_object.yolo_enable,
        running                 = shared_memory_object.running
    )

    #create processes
    zed_process                 = Process(target=vis.run_loop)
    #reader_process              = Process(target=shm.run_loop)
    kill_button_listener_process = Process(target=kill_button_listener.run_loop)
    depth_sensor_process        = Process(target=depth_sensor.run_loop)

    interface                   = Process(target=interface.run_loop)
    
    # start processes
    zed_process.start()
    #reader_process.start()
    kill_button_listener_process.start()
    depth_sensor_process.start()
    interface.start()

    # wait for processes to finish
    zed_process.join()
    #reader_process.join()
    kill_button_listener_process.join()
    depth_sensor_process.join()
    interface.join()

if __name__ == '__main__':
    print("RAW FROM LAUNCH")
    main()
