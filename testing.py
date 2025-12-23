import time, multiprocessing

start_time = time.perf_counter()

def sleep_a_second(duration):
    print(f"Start {duration} seconds of sleep")
    time.sleep(duration)
    print(f"Slept for {duration} seconds")

if __name__ == '__main__':

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=sleep_a_second, args=[1.25])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


    end_time = time.perf_counter()

    print(f"Time taken: {round(end_time - start_time, 2)} seconds")