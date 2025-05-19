from palindrome import *

from palindrome import *

def main():
    # Test is_palindrome function
    print("Testing is_palindrome...")
    examples_is_palindrome = [
        "racecar", "level", "hello", "noon", "world", 
        "radar", "madam", "python", "civic", 
        "step on no pets", "deified", "repaper", "was it a car or a cat I saw"
    ]
    for example in examples_is_palindrome:
        if is_palindrome(example):
            print(f"'{example}' is a palindrome.")
        else:
            print(f"'{example}' is not a palindrome.")

    

    # Test max_palindrome function
    print("\nTesting max_palindrome...")
    examples_max_palindrome = [
        "racecar", "level", "hello", "noon", "world", 
        "radar", "madam", "python", "civic", 
        "forgeeksskeegfor", "babad", "cbbd", "abacdedcaba"
    ]
    for example in examples_max_palindrome:
        result = max_palindrome(example)
        print(f"Longest palindromic substring in '{example}' is '{result}'.")

    

if __name__ == "__main__":
    main()
    
"""
Testing is_palindrome...
'racecar' is a palindrome.
'level' is a palindrome.
'hello' is not a palindrome.
'noon' is a palindrome.
'world' is not a palindrome.
'radar' is a palindrome.
'madam' is a palindrome.
'python' is not a palindrome.
'civic' is a palindrome.
'step on no pets' is a palindrome.
'deified' is a palindrome.
'repaper' is a palindrome.
'was it a car or a cat I saw' is not a palindrome.

Testing max_palindrome...
Longest palindromic substring in 'racecar' is 'racecar'.
Longest palindromic substring in 'level' is 'level'.
Longest palindromic substring in 'hello' is 'll'.
Longest palindromic substring in 'noon' is 'noon'.
Longest palindromic substring in 'world' is 'w'.
Longest palindromic substring in 'radar' is 'radar'.
Longest palindromic substring in 'madam' is 'madam'.
Longest palindromic substring in 'python' is 'p'.
Longest palindromic substring in 'civic' is 'civic'.
Longest palindromic substring in 'forgeeksskeegfor' is 'geeksskeeg'.
Longest palindromic substring in 'babad' is 'bab'.
Longest palindromic substring in 'cbbd' is 'bb'.
Longest palindromic substring in 'abacdedcaba' is 'abacdedcaba'.

"""
