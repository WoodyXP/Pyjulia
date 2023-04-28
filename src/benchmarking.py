from pylia import Pylia
import time

julia_module = Pylia("./example.jl")

def get_average_runtime(num_of_tests: int, args: list) -> float:
    runtimes = []
    for _ in range(num_of_tests):
        start_time = time.time()
        julia_module.call_func("dotp", args)
        end_time = time.time()
        runtimes.append(end_time - start_time)

    runtime_sum = 0.0
    for runtime in runtimes:
        runtime_sum += runtime

    return runtime_sum/num_of_tests

args = [2, 3, 4, 5]
print(f"The average runtime for the dotp function was: {get_average_runtime(50, args)} seconds")
