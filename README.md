# Pylia
Pylia is a python module for calling julia functions inside your python code.

## Usage
The julia interpreter is inside the PATH for the following examples. If you do not have julia inside your PATH you can also define the path to the julia interpreter like that:
```python
import pylia

julia_module = pylia.Julia("./example.jl")
julia_module.julia_interpreter = "your path to julia interpreter"

# execute code...
```

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
### call_func method
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
### using dynamic function declaration
Let's use the same ```example.jl``` from before. This means the content will look like this:
```julia
using Fire

@main function add(num::Integer...)
    println(sum(num))
end

@main function multiply(num::Integer...)
    println(prod(num))
end
```
Now in order to call these function within your python code you need to do this:
> ⚠️ **_NOTE:_**  Your IDE/text editor may tell you "Unresolved attribute reference add/multiply for class Julia". There's no need to worry. It should still work just as fine.
```python
import pylia

julia_module = pylia.Julia("./example.jl")

output = julia_module.add(my_args)
output2 = julia_module.multiply(my_args)
print(output, output2)
```
Your output should still look like this:
```
10 30
```
