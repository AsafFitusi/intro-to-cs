"""
student: Asaf Fitusi
ID:318763430
Assignment no.5
program: enc_dec
"""
"""
This program implements encryption and decryption using the Vigenère cipher. Users can choose to either encrypt or decrypt a text file. 
For encryption, the program filters out non-alphabetic characters, encrypts the text with a given key, and saves the result to a new file with _vig in the filename. 
For decryption, it reverses the process and saves the output with _dec in the filename.
"""
def add_letters(s1,s2):#This function creates the basic code based on the requirements.
    code_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 
             'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
             'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
             'w': 22, 'x': 23, 'y': 24, 'z': 25}
    reversed_code_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
                      8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
                      15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
                      22: 'w', 23: 'x', 24: 'y', 25: 'z'}   
    try:
        if len(s1) == 1 and len(s2) == 1 and s1[0].isalpha() and s2[0].isalpha():#Checks the condition for valid input.
            result1 = code_dict[s1.lower()] + code_dict[s2.lower()]
            if result1 > 25:
                mod_result1 = result1 % 26
                return reversed_code_dict[mod_result1]
            else:
                return reversed_code_dict[result1]
        else:
            return None           
    except Exception as e:
        print(e) 
          
def add_strings(s1, s2):#This function uses the ‘add_letters’ function to encrypt strings.
    length = len(s1)
    if len(s2) < length:
         length = len(s2)
    emy_str = ''
    try:
        if not s1.isalpha() or not s2.isalpha():#This condition ensures that the strings contain only letters.
            return None
        else:
            for i in range(length):
                x = add_letters(s1[i], s2[i])
                emy_str += x
            return emy_str
        
    except Exception as e:
        print(e)

def vigenere_encrypt(s, k):#This function creates the encrypted text using the Vigenère cipher.
    t = k
    try:
        if not t.isalpha() or not k.isalpha():
            return None
        else:
            if len(t) == len(s):#Checks if the strings are of the same length and ready for encryption.
                return add_strings(s, t)
            else:
                while len(t) < len(s):#This loop prepares the ‘t’ string for encryption.
                    t += t
                return add_strings(s, t)
    except Exception as e:
        print(e)

def vigenere_decrypt(w, k):#This function creates the decrypted text using the Vigenère cipher.
    code_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 
             'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
             'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
             'w': 22, 'x': 23, 'y': 24, 'z': 25}
    reversed_code_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
                      8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
                      15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
                      22: 'w', 23: 'x', 24: 'y', 25: 'z'}   
    t = k
    try:
        if not k.isalpha():
            return None
        else:
            while len(t) < len(w):#This loop prepares the ‘t’ string for decryption.
                t += t
            decrypted = ''
            for i in range(len(w)):#This loop decrypts each character of the encrypted text by subtracting the key values.
                w_value = code_dict[w[i].lower()]
                t_value = code_dict[t[i].lower()]
                result = (w_value - t_value) % 26
                decrypted += reversed_code_dict[result]
            return decrypted        
    except Exception as e:
        print(e)    

def main():#This is the main function of the program.
    try:
        e_d = input("Hello, and welcome to enc_dec.\nPlease choose between 'e' (encrypt) or 'd' (decrypt): ")
        if e_d == 'e':#The user chose to encrypt
            key = input("Please enter an encryption key (letters only, no spaces): ")
            file_name = input("Please enter the name of the file (including the .txt extension): ") 
            input_file = open(f'{file_name}', 'r')  
            file_content = input_file.read()  
            input_file.close()
            new_file_content = ''.join(char for char in file_content if char.isalpha())  
            file_res = vigenere_encrypt(new_file_content, key)
            dot_index = -1 
            for i in range(len(file_name)):#Loop through the file name to find the last dot
                if file_name[i] == '.':
                    dot_index=i
            if dot_index!=-1:  
                base_name=file_name[:dot_index]  
                extension=file_name[dot_index:]  
                output_file_name=base_name+"_vig"+extension
            else:
                output_file_name = file_name + "_vig"  
            output_file = open(output_file_name, 'w')  
            output_file.write(str(file_res))  
            output_file.close()
            print(f"The encrypted file has been saved as: {output_file_name}")
        elif e_d == 'd':#The user chose to decrypt
            key = input("Please enter an encryption key (letters only, no spaces): ")  
            file_name = input("Please enter the name of the file (including the .txt extension): ")  
            input_file = open(f'{file_name}', 'r') 
            file_content = input_file.read()  
            new_file_content = ''.join(char for char in file_content if char.isalpha())#Filter out non-alphabetic characters.
            file_res = vigenere_decrypt(new_file_content, key)#Decrypt the filtered content using the Vigenère cipher.
            input_file.close()  
            output_file_name = file_name.replace('_vig', '_dec')  
            output_file = open(output_file_name, 'w')  
            output_file.write(str(file_res))  
            output_file.close() 
            print(f"The decrypted file has been saved as: {output_file_name}")
        else:#The user entered invalid input
             print("You entered wrong values, program stopped.")  
    except Exception as e:
        print(e) 
if __name__ == "__main__":
    main()
        

