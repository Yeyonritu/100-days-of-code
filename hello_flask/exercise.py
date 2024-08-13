import time
current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

#Code below 👇

def speed_calc_decorator(function):
    
    def function_speed():
      function()
      
    return function_speed
      

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
fast_function()
end_time = time.time()

slow_function()
slow_time = time.time()

fast_function_time = end_time - current_time

slow_function_time = slow_time - current_time

print(f"{fast_function_time:.4f}seconds vs {slow_function_time:.4f}seconds")