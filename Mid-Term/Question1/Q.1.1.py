def sum_even_numbers(numbers):
    # Initialize a variable to store the sum of even numbers
    even_sum = 0

    # Iterate through the list and add even numbers to the sum
    for number in numbers:
        if number % 2 == 0:
            even_sum += number

    return even_sum

# Read a list of integers from the user, assuming they are separated by spaces
input_str = input("Enter a list of integers separated by spaces: ")
numbers = list(map(int, input_str.split()))

# Call the function to calculate the sum of even numbers
result = sum_even_numbers(numbers)

# Display the result
print("Sum of even numbers:", result)
