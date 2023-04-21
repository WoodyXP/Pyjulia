# Pylia
Pylia is a python module for calling julia functions inside your python code.

## Usage
You will have to use the [Fire](https://github.com/ylxdzsw/Fire.jl) package inside of your Julia code in order to use it like a cli application. An example would look like this:
```julia
using Fire

@main function add(num::Integer...)
    println(sum(num))
end

@main function multiply(num::Integer...)
    println(prod(num))
end
```

Let's say the content of this julia code belongs to a file called ```example.jl```. You can now call the add and multiply functions inside your python code:
```python
import pylia

julia_module = pylia.Julia("./example.jl")

my_args = [2, 3, 5]

julia_sum = julia_module.call_func("add", my_args)
julia_prod = julia_module.call_func("multiply", my_args)

print(julia_sum, julia_prod)
```
Your output should now look like this:
```
10 30
```
