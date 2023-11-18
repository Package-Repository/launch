import os
#"/vision/vision/vision_main.py"
def main():
    os.system('checkscript.sh')
    processid = os.fork()

    if processid == 0:
        print("main process")
    else:
        print("child process")
        os.system('python3 ./vision/vision/vision_main.py')


if __name__ == '__main__':
    main()