from typing import List

# Function to return a list of even integers from a given list
def even_list(int_list: List[int]) -> List[int]:
    """Determines if a number is even and returns an even list.
    
    Args:
        int_list: A list of integers.
    
    Returns:
        A list of even integers.
    """
    even_int_list = []
    for num in int_list:
        if num % 2 == 0:
            even_int_list.append(num)
    return even_int_list

# Function to compute the sum of squares of even integers in a given list
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """Computes the sum of the squares of all even numbers in a list of integers.
    
    Args:
        even_int_list: A list of even integers.
    
    Returns:
        The sum of the squares of all even numbers in the list.
    """
   # TODO: Implement sum_of_squares_of_even
    pass

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code
if __name__ == "__main__":
    main()