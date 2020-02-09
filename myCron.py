
import time
import cronSched


def sleepyTime(sleepTime):
    while True:
        cronSched.main()
        time.sleep(sleepTime)


if __name__ == '__main__':
    sleepyTime(900)
    # sleepyTime(float(sys.argv[1]))

