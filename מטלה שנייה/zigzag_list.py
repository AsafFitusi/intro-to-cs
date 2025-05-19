"""""
student: Asaf Fitusi
ID:318763430
Assignment no.2
program:zigzag_list

"""
def find_longest_zigzag(lst):
    """
    Finds the longest zigzag subsequence in the list.
    A zigzag alternates between increasing and decreasing directions of numbers.
    """
    if len(lst) < 2:
        return lst

    longest_zigzag = []
    current_zigzag = []

    for i in range(len(lst)):
        if len(current_zigzag) < 2:
            current_zigzag.append(lst[i])
        else:
            if (current_zigzag[-1] > current_zigzag[-2] and lst[i] < current_zigzag[-1]) or \
               (current_zigzag[-1] < current_zigzag[-2] and lst[i] > current_zigzag[-1]):
                current_zigzag.append(lst[i])
            else:
                if len(current_zigzag) > len(longest_zigzag):
                    longest_zigzag = current_zigzag[:]
                current_zigzag = [current_zigzag[-1], lst[i]]

    
    if len(current_zigzag) > len(longest_zigzag):
        longest_zigzag = current_zigzag

    return longest_zigzag

def get_list():
    """
    Reads a line of integers separated by commas and returns them as list.
    """
    input_line = input("Enter a list of integers separated by commas: ")
    return [int(x.strip()) for x in input_line.split(",")]

def main():
    """
    this function find and then print the longest zigzag sequence.
    """
    numbers = get_list() 
    result = find_longest_zigzag(numbers)  
    print("Longest zigzag sequence:", end=" ")
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i], end="")
        else:
            print(result[i], end=", ")

main()