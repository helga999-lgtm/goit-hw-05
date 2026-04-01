def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(f"Фібоначчі(10): {fib(10)}")  
print(f"Фібоначчі(15): {fib(15)}") 

print(f"Повторний виклик (10): {fib(10)}")