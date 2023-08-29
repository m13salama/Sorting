import threading
import time

def sleep_sort(arr):
    threads = []

    def thread_func(num):
        time.sleep(num / 100)
        print(num, end=" ")

    for num in arr:
        thread = threading.Thread(target=thread_func, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    arr = [54, 23, 1220, 9]
    sleep_sort(arr)
