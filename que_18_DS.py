import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper

@timer
def even_sorter(Input):
  output= []
  for val in Input:
    if val%2==0:
      output.append(val)
  time.sleep(2)
  return output
