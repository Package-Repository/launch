from multiprocessing import Value, Array


class SharedMemory:
    def __init__(self):
        self.imu_lin_acc            = Array('d', 3)
        self.imu_ang_vel            = Array('d', 3)
        self.imu_orientation        = Array('d', 3)
        self.distance_from_object   = Value('d', 0)
        self.yolo_offset            = Array('d', 2)
        self.color_offset           = Array('d', 2)
        self.color_enable           = Value('b', False)
        self.yolo_enable            = Value('b', False)
        self.gate_enable            = Value('b', False)
        self.current_color_index    = Value('i', 0)
        self.depth                  = Value('d', 0) 
        self.running                = Value('i', 1)
    