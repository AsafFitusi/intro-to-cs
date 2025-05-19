"""
student: Asaf Fitusi
ID: 318763430
Assignment no. 5
program: generate_partitions
"""
"""
Generates all possible partitions of integers from an input file using recursion. 
Each partition is a combination of numbers that sum up to the integer, written in descending order, and the results are saved to an output file.
"""
def get_partitions_helper(n,current_partition,all_partitions,max_size,current_index):#This recursive function generates all partitions of n in descending order and stores them in all_partitions.
   try:
       if n==0:
           all_partitions.append(current_partition[:])
           return
       for i in range(max_size,current_index-1,-1):#Iterates from max_size to current_index in reverse to build partitions in descending order.
           if i<=n:
               current_partition.append(i)
               get_partitions_helper(n-i,current_partition,all_partitions,i,current_index)
               current_partition.pop()
   except Exception as e:
        print(e)
def get_partitions(n):#This function returns all partitions of n by calling the recursive helper function.
    try:
        all_partitions=[]
        get_partitions_helper(n,[],all_partitions,n,1)
        return all_partitions
    except Exception as e:
         print(e)
def main():#This is the main function of the program.
    input_file="partition_sizes.txt"
    output_file="partitions.txt"    
    try:
        content = open(input_file).read().strip()
        if not content:
            raise ValueError("Input file is empty.")
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    valid_numbers=[]
    for item in content.split():#Iterates through the input content,converts each item to an integer,and appends it to valid_numbers if it’s positive,ignoring invalid entries.
        try:
            number=int(item)
            if number>0:
                valid_numbers.append(number)
        except ValueError:
            continue
    try:
        file = open(output_file, 'w')  
        for number in valid_numbers:#Iterates through valid_numbers,generates partitions for each number,and writes a header for the partitions to the output file.
            partitions=get_partitions(number)
            file.write(f"partitions for {number}:\n")
            for partition in partitions:#Iterates through each partition of the current number and writes it to the output file in a comma-separated format,followed by a blank line.
                file.write(f"{', '.join(map(str, partition))}\n")
            file.write("\n")
        file.close()
    except Exception as e:
        print(f"Error writing to output file: {e}")
if __name__=="__main__":
    main()