# Pylia
Pylia is a python module for calling julia functions inside your python code.

## Usage
The julia interpreter is inside the PATH for the following examples. If you do not have julia inside your PATH you can also define the path to the julia interpreter like that:
```python
import pylia

julia_module = pylia.Pylia("./example.jl")
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

@main function greet(name, age, num::Integer...)
    println(name, age)
    println(num)
end
```
### call_func method
Let's say the content of this julia code belongs to a file called ```example.jl```. You can now call the add and multiply functions inside your python code:
```python
import pylia

julia_module = pylia.Pylia("./example.jl")

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

@main function greet(name, age, num::Integer...)
    println(name, age)
    println(num)
end
```
Now in order to call these function within your python code you need to do this:
> ⚠️ **_NOTE:_**  Your IDE/text editor may tell you "Unresolved attribute reference add/multiply for class Julia". There's no need to worry. It should still work just as fine.
```python
import pylia

julia_module = pylia.Pylia("./example.jl")

output = julia_module.add(my_args)
output2 = julia_module.multiply(my_args)
print(output, output2)
```
Your output should still look like this:
```
10 30
```

The ```greet``` function inside the julia file has multiple arguments. But this doesn't prevent us from calling it from python. It works just as fine as the other examples above:
```python
import pylia

julia_module = pylia.Pylia("./example.jl")
greet_args = ["Pylia", 19, 2, 3, 4, 5]
greeting = julia_module.greet(greet_args)
print(greeting)
```
The following output should be printed to the terminal:
```
Pylia19
(2, 3, 4, 5)
```
You can just treat them as normal positional variables and the [Fire](https://github.com/ylxdzsw/Fire.jl) package from julia will parse the arguments automatically.