def generateFibonacci(length):
    # Defines an empty list for sequence
    fibonacci_sequence = []

    # Defines edge cases
    higher = 1
    lower = 1

    # Calculating
    for i in range(length):
        fibonacci_sequence.append(lower)  # Adding lower (or previously calculated) Fibonacci to the list
        nextHigher = lower + higher  # Calculating next higher Fibonacci
        lower = higher  # Shift to next position
        higher = nextHigher  # Shift to next position
    print("Length of Fibonacci sequence is: ", length)
    print("Fibonacci sequence is: ",fibonacci_sequence)
    print("")
    return fibonacci_sequence


# Defines user input

# length = int(input("How many numbers from the Fibonacci sequence do you want to get? "))

# Screen output
# print(fibonacci_sequence)
