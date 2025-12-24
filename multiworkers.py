import multiprocessing
import time

def do_work(worker_id, output_queue):
    time.sleep(1)
    result = f"Data from worker {worker_id}"
    output_queue.put(result)

if __name__ == "__main__":
    my_queue = multiprocessing.Queue()
    processes = []

    for i in range(1, 4):
        p = multiprocessing.Process(target=do_work, args=(i, my_queue))
        processes.append(p)
        p.start()

    for _ in range(3):
        data = my_queue.get()
        print(f"Boss received: {data}")

    for p in processes:
        p.join()