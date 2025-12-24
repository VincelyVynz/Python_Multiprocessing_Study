import time, multiprocessing


def worker_task(worker_id, parking_lot):
    print(f"Worker {worker_id} is looking for a parking spot")

    with parking_lot:
        print(f"Worker {worker_id} is parked")
        time.sleep(1.5)
        print(f"Worker {worker_id} is leaving the parking lot")


if __name__ == "__main__":

    parking_lot = multiprocessing.Semaphore(2)

    processes = [multiprocessing.Process(target=worker_task, args=(i, parking_lot)) for i in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()