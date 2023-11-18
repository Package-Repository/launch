import os
from vision.vision.vision_main import VideoRunner
#"/vision/vision/vision_main.py"
def main():
    
    processid = os.fork()

    if processid == 0:
        print("main process")
    else:
        print("child process")
        vis = VideoRunner()
        vis.run_loop()


if __name__ == '__main__':
    main()