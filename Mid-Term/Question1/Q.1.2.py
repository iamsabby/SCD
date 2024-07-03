def count_vowels(string):
    # Convert the string to lowercase to make it case-insensitive
    string = string.lower()
    
    # Initialize a variable to keep track of the vowel count
    vowel_count = 0
    
    # Define a set of vowels to check against
    vowels = set("aeiou")
    
    # Iterate through the characters in the string
    for char in string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

input_string = "Sabih Ul Hassan"
result = count_vowels(input_string)
print("Number of vowels:", result)
