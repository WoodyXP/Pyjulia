#import pylia
from julia_file import JuliaFile


#julia_module = pylia.Julia("./example.jl")
#
#my_args = [2, 3, 5]
#
#julia_sum = julia_module.call_func("add", my_args)
#julia_prod = julia_module.call_func("multiply", my_args)
#
#print(julia_sum, julia_prod)
#
#
#julia_module.add_custom_method("add", my_args)
#custom_class = CustomClass()
#

# Call the actual function
juliaFile = JuliaFile("./example.jl", ["add"])
juliaFile.add([2, 3, 5])
