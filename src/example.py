import pylia

julia_module = pylia.Julia("./example.jl")

my_args = [2, 3, 5]

# julia_sum =julia_module.call_func("add", my_args)
julia_functions = julia_module.get_funcs()

print(julia_functions)
