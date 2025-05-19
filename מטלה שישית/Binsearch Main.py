from binsearch import *

def main():
    # Example sorted list
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]

    # Test cases
    numbers_to_find = [7, 1, 15, 4, 9, 20]

    print("Binary Search Results:")
    for num in numbers_to_find:
        result = binsearch(sorted_list, num)
        if result is not None:
            print(f"Number {num} found at index {result}.")
        else:
            print(f"Number {num} not found in the list.")

if __name__ == "__main__":
    main()
    
"""
Binary Search Results:
Number 7 found at index 3.
Number 1 found at index 0.
Number 15 found at index 7.
Number 4 not found in the list.
Number 9 found at index 4.
Number 20 not found in the list.
"""

