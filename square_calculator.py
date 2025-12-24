import multiprocessing
import time


def square_number(n):
    time.sleep(1)  # Simulating a heavy calculation
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # --- CHANGE THE CODE BELOW THIS LINE ---
    with multiprocessing.Pool() as pool:
        results = pool.map(square_number, numbers)
    # --- CHANGE THE CODE ABOVE THIS LINE ---

    print(f"Squares: {results}")