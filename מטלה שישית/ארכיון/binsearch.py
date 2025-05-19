"""
student: Asaf Fitusi
ID:318763430
Assignment no.6
program: binsearch.py
"""

def binsearch(lst,num,start_index=0):
    if len(lst)==0:
        return None
    mid=len(lst)//2
    if lst[mid]==num:
        return start_index+mid
    elif lst[mid]<num:
        return binsearch(lst[mid + 1:], num, start_index + mid + 1)
    else:
        return binsearch(lst[:mid], num, start_index)
    
def main():
    lst=[2,3,5,7,11,13,17,19,23,29]
    num=23
    result=binsearch(lst, num)
    print(result)
    
    
if __name__ == "__main__":
    main()