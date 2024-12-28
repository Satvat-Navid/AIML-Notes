'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Senario: Factorial Calculation
Factorial calculation, especially for large numbers, 
involve significant computational work, MultiProcessing
can be used to distribute the workload across multiple
CPU cores, improving performance.
'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# funtion to compute factorials of a given number

def compute_factorial(number):
    print(f"Computing Factorial of {number}")
    result = math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

    numbers = [5000, 6000, 700, 8000]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Result {results}")
    print(f"Time taken: {start_time - end_time} seconds")

