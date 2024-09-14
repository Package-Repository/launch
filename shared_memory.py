from multiprocessing import Value, Array


class SharedMemoryWrapper:
    def __init__(self):
        self.imu_lin_acc            = Array('d', 3)
        self.imu_ang_vel            = Array('d', 3) #p y r
        self.imu_orientation        = Array('d', 3)
        self.distance_from_object   = Value('d', 0)
        self.yolo_offset            = Array('d', 2)
        self.color_offset           = Array('d', 2)
        self.gate_offset            = Array('d', 2)
        self.color_enable           = Value('b', False)
        self.yolo_enable            = Value('b', False)
        self.gate_enable            = Value('b', False)
        self.current_color_index    = Value('i', 0)
        self.depth                  = Value('d', 0) 
        self.running                = Value('i', 1)

        self.dvl_yaw                = Value('d', 0)
        self.dvl_pitch              = Value('d', 0)
        self.dvl_roll               = Value('d', 0)
        self.dvl_x                  = Value('d', 0)
        self.dvl_y                  = Value('d', 0)
        self.dvl_z                  = Value('d', 0)

        self.dvl_x_velocity         = Value('d', 0)
        self.dvl_y_velocity         = Value('d', 0)
        self.dvl_z_velocity         = Value('d', 0)
        self.dvl_velocity_valid     = Value('b', False)
        self.dvl_status             = Value('b', False)
        self.dvl_altitude           = Value('d', 0)

        self.target_x               = Value('d', 0)
        self.target_y               = Value('d', 0)
        self.target_z               = Value('d', 0)
        self.target_yaw             = Value('d', 0)
        self.target_pitch           = Value('d', 0)
        self.target_roll            = Value('d', 0)
    