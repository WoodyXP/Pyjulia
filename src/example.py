import pylia

julia_module = pylia.Julia("./example.jl")

my_args = [2, 3, 5]

# julia_sum = julia_module.call_func("add", my_args)
# julia_prod = julia_module.call_func("multiply", my_args)

# print(julia_sum, julia_prod)

print(julia_module.functions)
