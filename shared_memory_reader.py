from multiprocessing import Process, Value
from subprocess import call

'''
    discord: @kialli
    github: @kchan5071
    
    test class to read from shared memory and print values
    
'''

class SharedMemoryReader:
    def __init__(self, linear_acceleration_x , linear_acceleration_y, linear_acceleration_z, 
                angular_velocity_x, angular_velocity_y, angular_velocity_z, 
                orientation_x, orientation_y, orientation_z, 
                depth,
                offset_x, offset_y):
        self.linear_acceleration_x = linear_acceleration_x
        self.linear_acceleration_y = linear_acceleration_y
        self.linear_acceleration_z = linear_acceleration_z
        self.angular_velocity_x = angular_velocity_x
        self.angular_velocity_y = angular_velocity_y
        self.angular_velocity_z = angular_velocity_z
        self.orientation_x = orientation_x
        self.orientation_y = orientation_y
        self.orientation_z = orientation_z
        self.depth = depth
        self.offset_x = offset_x
        self.offset_y = offset_y
        
    def run_loop(self):
        while True:
            print("linear_acceleration_x: ", self.linear_acceleration_x.value)
            print("linear_acceleration_y: ", self.linear_acceleration_y.value)
            print("linear_acceleration_z: ", self.linear_acceleration_z.value)
            print("angular_velocity_x: ", self.angular_velocity_x.value)
            print("angular_velocity_y: ", self.angular_velocity_y.value)
            print("angular_velocity_z: ", self.angular_velocity_z.value)
            print("orientation_x: ", self.orientation_x.value)
            print("orientation_y: ", self.orientation_y.value)
            print("orientation_z: ", self.orientation_z.value)
            print("depth: ", self.depth.value)
            print("offset_x: ", self.offset_x.value)
            print("offset_y: ", self.offset_y.value)
            print("--------------------------------------------------")
            call('clear')