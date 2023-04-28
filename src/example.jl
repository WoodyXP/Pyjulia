using Fire

@main function add(num::Integer...)
    println(sum(num))
end

@main function multiply(num::Integer...)
    println(prod(num))
end

@main function greet(name)
    println(name)
end

@main function dotp(nums::Integer...)
    vec1 = nums[1:(length(nums)/2)]
    vec2 = nums[((length(nums)/2)+1):length(nums)]

    dotproduct = 0.0
    i = 1
    while i <= length(vec1)
        dotproduct += vec1[i] * vec2[i]
        i += 1
    end
    println(dotproduct)
end