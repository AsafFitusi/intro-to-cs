"""
student: Asaf Fitusi
ID:318763430
Assignment no.6
program: dict.py
"""

def join_dict(d1,d2):
    new_ls=[]
    if len(d1)>=len(d2):
        for item1 in d1.items():
            for item2 in d2.items():
                if item1[0]==item2[0]:
                    tup=item1[1],item2[1]
                    new_ls.append(tup)
    if len(d2)>len(d1):
        for item2 in d2.items():
            for item1 in d1.items():
                if item1[0]==item2[0]:
                    tup=item1[1],item2[1]
                    new_ls.append(tup)
               
    return (new_ls)

def is_mutual(tpl,d1,d2):
    ls=join_dict(d1,d2)
    if tpl in ls:
        return True
    return False
           
def main():
    d1=dict(input('enter the first dict: '))
    d2=dict(input('enter the second dict: '))
    tpl=tuple(input('enter the tuple you want to check'))
    is_mutual(tpl,d1,d2)
if __name__ == "__main__":
    main()
        

