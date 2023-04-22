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
