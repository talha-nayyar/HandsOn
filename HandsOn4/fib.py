def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Step into all recursive calls for fib(5)
def trace_fib(n, depth=0):
    print("  " * depth + f"fib({n})")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return trace_fib(n-1, depth+1) + trace_fib(n-2, depth+1)

print("Tracing Fibonacci Calls for fib(5):")
trace_fib(5)