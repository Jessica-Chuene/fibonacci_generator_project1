def fibonacci(n: int):
    # Base case: handles the edges
    if n < 0:
        return
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case:
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # iterate through n in a list
    fib_sequence = [fibonacci(i) for i in range(int(input("Enter a number to generate: ")))]
    print(fib_sequence)
