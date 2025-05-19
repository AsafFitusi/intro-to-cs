"""
student: Asaf Fitusi
ID:318763430
Assignment no.4
program: poly_matrix
"""
""""
This program processes a text file containing matrices and polynomials. For each matrix and its corresponding polynomial, the program calculates the result of applying the polynomial to the matrix. It writes the results into an output file, with each resulting matrix formatted neatly.
"""

def matrix_scalar_mult(A, c):#This function that creates a matrix multiplied by a scalar.
    Ac = [[e * c for e in row] for row in A]
    return Ac

def matrix_add(A, B):#This function that adds two matrices.
    AsumB = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return AsumB

def matrix_mult(A, B):#This function that multiplies two matrices.
    AmultB = [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
    return AmultB

def identity_matrix(n):#This function that creates the identity matrix.
    In = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return In

def matrix_polynom(A, p):#This function that calculates the polynomial of a matrix.
    emy_mat = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    result = emy_mat
    for i in range(len(p)):#Iterate over the polynomial coefficients.
        if i == 0:
            Ip = identity_matrix(len(A))
            I_scalar_p = matrix_scalar_mult(Ip, p[i])
            result = matrix_add(result, I_scalar_p)
        elif i == 1:
            As = matrix_scalar_mult(A, p[i])
            result = matrix_add(result, As)
        else:
            A_mult = A
            for j in range(i - 1):#Multiply A by itself (i-1) times.
                A_mult = matrix_mult(A_mult, A)
            A_mult_scaled = matrix_scalar_mult(A_mult, p[i])
            result = matrix_add(result, A_mult_scaled)
    return result

def str_to_matrix(string):#This function turns a string into a matrix.
    parts = string.split('\n')[0].split()  
    len_mat = int(parts[0])  
    float_lst_string = [float(item) for item in parts[1:]] 
    lst_to_matrix = [float_lst_string[i:i + len_mat] for i in range(0, len(float_lst_string), len_mat)]
    return lst_to_matrix

def print_matrix(A, output_file):#This function gets a matrix and prints the matrix to the file.
    for row in A:
        output_file.write(' '.join(f'{value:10.2f}' for value in row) + '\n')  

def matrix_input(input_file):#This function processes the input file content.
    count = 0
    results = []
    for row in input_file:#This loop goes through every line in the input file.
        row = row.replace('\n', '')  
        count += 1
        if count % 2 == 1:            
            matrix = str_to_matrix(row)
        else:  
            polynomial = [float(num) for num in row.split()]
            result = matrix_polynom(matrix, polynomial)
            results.append(result)
    return results

def main():#The main function of the program.
    input_file = open('Matrix Input.txt', 'r')
    results = matrix_input(input_file)
    input_file.close()

    output_file = open('matrix_output.txt', 'w')
    for result in results:#This loop goes through every result and writes it to the output file.
        print_matrix(result, output_file)
        output_file.write('\n')  
    output_file.close()

main()