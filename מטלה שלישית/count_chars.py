"""""
student: Asaf Fitusi
ID:318763430
Assignment no.3
program:count_chars
"""
"""
This program takes a file from the user containing different strings and returns the total number of letters in the text,
 counting only one letter per word, even if the letter appears multiple times in the same word, and draws a histogram of the letter counts.
"""

def count_substring(alphabet, l_word,abc_count):#Counts the number of times a substring occurs within a given string.

    for let in alphabet:#Updates the count of each letter in the word, considering its position in the alphabet
        if let in l_word:
            abc_count[ord(let)-ord('a')]+=1
    return (abc_count)

def draw_histogram(count_let):#Draws a histogram that shows the occurrence of letters in the given string.
    height=max(count_let)
    for h in range(height):#Iterate over each row of the histogram from top to bottom
        for j in range(-1,-27,-1):#Iterate over the letters in reverse order (z to a)
           if count_let[j]>=height:
               print("+",end="")
           else:
               print(" ",end="")
        height-=1
        print()
    print("zyxwvutsrqponmlkjihgfedcba")
    
    
def count_letters(s):#Uses count_substring to count how many letters are in a word, ensuring that even if a letter appears multiple times in a word, it is counted only once.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    abc_count=[0]*26
    split_word=s.split()
    for word in split_word:#Iterate through each word in the input string, convert it to lowercase, and count the occurrences of each letter
        l_word=word.lower()
        count_let=count_substring(alphabet, l_word,abc_count)
    draw_histogram(count_let)
    
    
     
def main():#main function that gets the file from the user.
    file_loc = input("Enter a file name: ")
    file=open(file_loc, "r")
    str_file = file.read()
    file.close()
    count_letters(str_file)
    
main()