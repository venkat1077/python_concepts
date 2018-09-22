import threading
import time


def wait_for_timeout(thread_name, timeout):
    start_time = 0
    while start_time < timeout:
        time.sleep(1)
        start_time += 1
        print "remaining time in thread '{}' is {}.".format(thread_name, timeout-start_time)
    print "#### Thread {} is finished ####".format(thread_name)


try:
    threading.Thread(target=wait_for_timeout, args=('thread1', 10)).start()
    threading.Thread(target=wait_for_timeout, args=('thread2', 15)).start()
    threading.Thread(target=wait_for_timeout, args=('thread3', 5)).start()
except Exception as e:
    print "Errors in creating Threads : {}".format(e)
