from multiprocessing import Process, Value
from subprocess import call

class SharedMemoryReader:
    '''
        discord: @kialli
        github: @kchan5071
        
        test class to read from shared memory and print values
        
    '''
    def __init__(self,  linear_acceleration_x ,  linear_acceleration_y,  linear_acceleration_z, 
                        angular_velocity_x,      angular_velocity_y,     angular_velocity_z, 
                        orientation_x,           orientation_y,          orientation_z, 
                        distance,                depth,
                        yolo_offset_x,           yolo_offset_y,
                        color_offset_x,          color_offset_y,
                        color,
                        color_enable,            yolo_enable,
                        running):
        self.linear_acceleration_x = linear_acceleration_x
        self.linear_acceleration_y = linear_acceleration_y
        self.linear_acceleration_z = linear_acceleration_z
        self.angular_velocity_x = angular_velocity_x
        self.angular_velocity_y = angular_velocity_y
        self.angular_velocity_z = angular_velocity_z
        self.orientation_x = orientation_x
        self.orientation_y = orientation_y
        self.orientation_z = orientation_z
        self.distance = distance
        self.yolo_offset_x = yolo_offset_x
        self.yolo_offset_y = yolo_offset_y
        self.depth = depth

        self.color_offset_x = color_offset_x
        self.color_offset_y = color_offset_y
        self.color = color
        self.yolo_enable = yolo_enable
        self.running = running


        self.color_filter_enable = color_enable
        
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
            print("distance: ", self.distance.value)
            print("depth: ", self.depth.value)
            print("yolo_offset_x: ", self.yolo_offset_x.value)
            print("yolo_offset_y: ", self.yolo_offset_y.value)
            print("color_offset_x: ", self.color_offset_x.value)
            print("color_offset_y: ", self.color_offset_y.value)
            print("color: ", self.color.value)
            print("yolo enable: ", self.yolo_enable.value)
            print("color_enable: ", self.color_filter_enable.value)
            print("--------------------------------------------------")
            call('clear')