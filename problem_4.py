ef process_list(numbers, start_index, end_index):
    # Step 1: Create a new list of squares of even numbers using list comprehension
    squares_of_even_numbers = [x**2 for x in numbers if x % 2 == 0]

    # Step 2: Slice the original list to extract a sublist from start_index to end_index
    sublist = numbers[start_index:end_index]

    return squares_of_even_numbers, sublist

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_index = 2
end_index = 7

squares_of_even, sublist = process_list(original_list, start_index, end_index)

print("Original list:", original_list)
print("Squares of even numbers:", squares_of_even)
print("Sublist from index", start_index, "to", end_index, ":", sublist)
