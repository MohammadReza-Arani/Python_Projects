def fibonacci(n):
    if n<= 0:
        return "Invalid input. n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for k in range(2,n):
            c = a + b
            a = b
            b = c
        return b


#Ask user for input
n = int(input("Enter n as input: "))
result = fibonacci(n)
print(f"the {n}th Fibonacci term is: {result}")
