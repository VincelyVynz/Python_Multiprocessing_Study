import multiprocessing
import time

# Multiprocessing with Pool


def do_work(worker_id):
    time.sleep(1)
    return f"Data from worker {worker_id}"

if __name__ == "__main__":
    # Define the inputs we want to process
    work_list = [1, 2, 3, 4, 5]

    # Create a Pool of 5 worker processes
    with multiprocessing.Pool(processes=5) as pool:
        # map() sends each item in work_list to do_work
        results = pool.map(do_work, work_list)

    # All results are collected into a simple list!
    print(f"Boss received: {results}")



# Multiprocessing with Queue


# def do_work(worker_id, output_queue):
#     time.sleep(1)
#     result = f"Data from worker {worker_id}"
#     output_queue.put(result)
#
# if __name__ == "__main__":
#     my_queue = multiprocessing.Queue()
#     processes = []
#
#     for i in range(1, 4):
#         p = multiprocessing.Process(target=do_work, args=(i, my_queue))
#         processes.append(p)
#         p.start()
#
#     for _ in range(3):
#         data = my_queue.get()
#         print(f"Boss received: {data}")
#
#     for p in processes:
#         p.join()