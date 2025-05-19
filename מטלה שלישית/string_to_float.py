"""""
student: Asaf Fitusi
ID:318763430
Assignment no.3
program:string_to_float
"""
"""
This program gets a file from the user that contains different strings and returns the requested details about it.
"""
def is_float(strings):#Gets a string, checks if it contains valid real digits or not, and returns true or false along with the count of invalid strings.
    valid_floats = []
    invalid_count = 0

    for str in strings:#Iterates through each string to validate if it represents a valid float.
        count = 0
        is_valid = True

        if len(str) == 0:
            is_valid = False

        if is_valid and str[0] in "+-":
            if len(str) == 1 or not (str[1].isdigit() or str[1] == "."):
                is_valid = False

        if is_valid and str[0] == ".":
            is_valid = False  

        if is_valid and len(str) > 1 and str[0] == "0" and str[1] != ".":
            is_valid = False

        for c in str[1:] if str[0] in "+-" else str:#Iterates over all characters in the string, skipping the '+' or '-' sign if present at the start of the string.
            if c == ".":
                count += 1
                if count > 1:
                    is_valid = False
                    break
            elif not c.isdigit():
                is_valid = False
                break

        if is_valid and (str == "." or str[-1] == "."):
            is_valid = False

        if is_valid:
            valid_floats.append(float(str))
        else:
            invalid_count += 1

    return valid_floats, invalid_count

def string_to_float(str):#Checks the string with is_float for valid digits, converts the valid digits into a list, removes the invalid ones, and prints their count.   
    str_list = str.split()
    valid_floats, invalid_count = is_float(str_list)
    print(f"Minimum: {min(valid_floats):.2f}")
    print(f"Maximum: {max(valid_floats):.2f}")
    print(f"Mean: {sum(valid_floats) / len(valid_floats):.2f}")
    print(f"Legal Numbers: {len(valid_floats)}")
    print(f"Illegal Numbers: {invalid_count}")

def main():#Main function that gets the file from the user.
   file_loc = input("Enter a file name: ")
   f = open(file_loc, "r")
   str_file = f.read()
   f.close()
   string_to_float(str_file)
   
main()