import pylia

julia_module = pylia.Julia("./example.jl")

my_args = [2, 3, 5]

# you can either use call_func
julia_sum = julia_module.call_func("add", my_args)
julia_prod = julia_module.call_func("multiply", my_args)
print(julia_sum, julia_prod)

# or you can use dynamic func declaration
output = julia_module.add(my_args)
output2 = julia_module.multiply(my_args)
print(output, output2)

# you can also have multiple arguments
greet_args = ["Pylia", 19, 2, 3, 4, 5]
greeting = julia_module.greet(greet_args)
print(greeting)
