from loky import get_reusable_executor

# Example of process function
'''
def process(k):
    sleep(.01)
    print('Hello')
'''


# Create an executor with 4 worker processes, that will
# automatically shutdown after idling for 2s
# in range(50) pointed the admissible count of processes
def run(process, max_workers=4, timeout=2, process_count=50):
    executor = get_reusable_executor(max_workers=max_workers, timeout=timeout)
    executor.submit(process, 1)
    executor.map(process, range(process_count))
