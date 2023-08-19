#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0,1]

    while len(fibonacci) < length:
        nextNumber = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(nextNumber)
    
    for x in fibonacci:
        print(x)

print(print_fibonacci(9))