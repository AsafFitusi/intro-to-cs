"""
student: Asaf Fitusi
ID:318763430
Assignment no.6
program: intersection_NR.py
"""
import math

def difference(f, g, x):
    # Returns the difference between two functions f and g at point x
    return f(x) - g(x)

def deriv(f, x, h=0.000001):
    # Calculates the derivative of function f at point x using finite difference
    return (f(x + h) - f(x - h)) / (2 * h)

def NR(f, a, b, epsilon=10**-10, n=100):
    # Implements the Newton-Raphson method to find a root of f in [a, b]
    x0 = (a + b) / 2
    for i in range(n):  # Iterates up to n times to find the root
        fx0 = f(x0)
        dfx0 = deriv(f, x0)
        if abs(fx0) < epsilon:
            return x0
        if dfx0 == 0:
            return None
        x1 = x0 - fx0 / dfx0
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1
    return None

def intersection_NR(f, g, a, b, epsilon=10**-10, n=100):
    # Finds the intersection point of two functions f and g in [a, b]
    def h(x):
        return difference(f, g, x)
    return NR(h, a, b, epsilon, n)

def load_functions(file_path):
    # Loads functions from a file and converts them into callable Python functions
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()
    functions = []
    for line in lines:  # Processes each line to extract function definitions
        if line.strip():
            func_str = line.strip()
            func = eval(f"lambda x: {func_str}")
            functions.append(func)
    return functions

def main():
    # Main program to read functions, find intersection, and write the result to a file
    input_file = "input_functions.txt"
    output_file = "output_functions.txt"
    try:
        functions = load_functions(input_file)
        if len(functions) < 2:
            raise ValueError("The input file must contain at least two functions.")
        f, g = functions[:2]
        a, b = 1, 4  # Can modify the range here
        root = intersection_NR(f, g, a, b)
        file = open(output_file, "w")
        if root is not None:
            file.write(f"{root}\n")
        else:
            file.write("No intersection found.\n")
        file.close()
    except Exception as e:
        file = open(output_file, "w")
        file.write(str(e) + "\n")
        file.close()

if __name__ == "__main__":
    main()