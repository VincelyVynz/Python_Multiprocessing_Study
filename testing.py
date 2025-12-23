import time

def sleep_a_second():
    print("Start sleep")
    time.sleep(1)
    print("Slept")

if __name__ == '__main__':
    start_time = time.perf_counter()
    sleep_a_second()
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    print(time_taken)
    print(f"Time taken: {round(time_taken, 2)} seconds")
