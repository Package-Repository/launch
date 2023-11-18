import os

def main():
    os.system('checkscript.sh')
    vision = os.fork("/vision/vision/vision_main.py")
    

if __name__ == '__main__':
    main()