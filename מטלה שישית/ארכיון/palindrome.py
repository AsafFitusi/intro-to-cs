"""
student: Asaf Fitusi
ID:318763430
Assignment no.6
program: palindrome.py
"""

def is_palindrome(st):
    if len(st)==0:
        return True
    if st[0]==st[-1]:
        return is_palindrome(st[1:-1])
    else:
        return False

def max_palindrome(st):
    if is_palindrome(st):
        return st
    pali1=max_palindrome(st[1:])
    pali2=max_palindrome(st[:-1])
    if len(pali1)>len(pali2):
        return pali1
    else:
        return pali2
      
def main():
    st="abcd"
    pali_st=max_palindrome(st)
    print(pali_st)

if __name__ == "__main__":
    main()