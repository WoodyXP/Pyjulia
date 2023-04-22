import pylia

julia_module = pylia.Julia("./example.jl")
julia_module.julia_interpreter = "C:/Users/ruben/AppData/Local/Programs/Julia-1.8.3/bin/julia.exe"

my_args = [2, 3, 5]

# you can either use call_func
julia_sum = julia_module.call_func("add", my_args)
julia_prod = julia_module.call_func("multiply", my_args)
print(julia_sum, julia_prod)

# or you can use dynamic func declaration
output = julia_module.add(my_args)
output2 = julia_module.multiply(my_args)
print(output, output2)
