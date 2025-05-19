"""""
student: Asaf Fitusi
ID:318763430
Assignment no.3
program:traingle
"""
"""
The user types-in a string and the program creates the smallest possible traingle from that string. Type quit to stop.
"""
def string_in_flip_triangle(phrase):# This function creates the triangle.
    phrase_len=len(phrase)
    triangle_output = ""
    sqrt_len=(phrase_len**0.5)#Iused Inbal’s calculation, where we needed to calculate the square root of the string length.
    
    if sqrt_len== int(sqrt_len):
        rows=int(phrase_len**0.5)+2
    else:
        rows=int(phrase_len**0.5)+3
    
    base_len=(rows*2)-1
    base_row="*"*base_len
    triangle_output +=base_row+"\n"
    
    char_position=0
    for row in range(2, rows):#Loop through each row of the triangle
        triangle_output+= " " * (row - 1) + "*" 
        spaces_between =base_len - 2 * row
        row_content=[]
        
        if char_position<phrase_len:
            for space in range(spaces_between):#Add characters between the stars
                if char_position<phrase_len:
                    row_content.append(phrase[char_position])
                    char_position+=1
                else:
                    row_content.append(" ")
            triangle_output +="".join(row_content)+"*"+"\n"
        else:
            triangle_output +=" "*(base_len-2*row)+"*"+"\n"
    
    if rows>1:
        triangle_output += " "*(rows-1)+"*\n"
    
    return triangle_output

def main():# Main function gets the input, calls the function 'string_in_flip_triangle', and repeats until 'quit'.
    phrase=input("Enter a phrase: ")
    while phrase!="quit":  # Keep asking for input until the user types "quit"
        print(string_in_flip_triangle(phrase))  
        phrase=input("Enter a phrase: ")  
    
main()