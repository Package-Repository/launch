from multiprocessing import Value, Array


class SharedMemoryWrapper:
    def __init__(self):
        #add properties here
        self.example_array          = Array('i', [1, 2, 3, 4, 5])
        self.running                = Value('b', True)

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
