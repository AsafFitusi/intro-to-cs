"""""
student: Asaf Fitusi
ID:318763430
Assignment no.2
program:flip_traingle
"""
def draw_triangle(height, char): #I used the code Guy provided us druing the practice session
    """
    Draws an inverted isosceles triangle of the specified height using the given character.
   "heigjt": The number of rows in the triangle.
    "char": The character used to draw the triangle.
    """
    for i in range(height, 0, -1):  
        spaces = height - i 
        if i == height:  
            print(" " * spaces + char * (2 * i - 1))
        else:
            if i == 1:  
                print(" " * spaces + char)
            else:  
                print(" " * spaces + char + " " * (2 * i - 3) + char)

def main():
    """
    this function  prompts the user for the triangle's height and character,
    and calls "draw_triangle" to draw it. Ensures the height is not more then 40.
    """
    height = int(input("Please enter triangle height (not more than 40): "))
    while height > 40:  
        print("Height needs to be 40 or less.")
        height = int(input("Please enter triangle height (not more than 40): "))
    
    char = input("Please enter triangle character: ")  
    draw_triangle(height, char)  

main()