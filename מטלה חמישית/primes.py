"""
student: Asaf Fitusi
ID:318763430
Assignment no.5
program: prime_miller_rabin (primes)
"""
"""
This program generates k unique m-digit prime numbers using the Miller-Rabin test and writes them to primes.txt, one per line.
"""
import prime_miller_rabin
def primes(k,m):#This function generates a list of prime numbers according to the specified requirements
    try:
        emy_ls=[]
        for num in range(k):#The loop generates k distinct prime numbers and adds them to the list.
            num=prime_miller_rabin.make_prime(m)
            if num not in emy_ls:
                emy_ls.append(num)
            else:
                while num in emy_ls:
                    num=prime_miller_rabin.make_prime(m)
                emy_ls.append(num)
        emy_str=''
        for num in emy_ls:#The loop inserts the prime numbers into the string.
                emy_str+=str(num)
                emy_str+='\n'
        return emy_str
    except Exception as e:
        print(e)
 
def main():#This is the main function of the program.
    k=int(input('Enter number of primes: '))
    m=int(input('Enter size of primes: '))
    str_primes=(primes(k,m))
    try: 
        file=open('primes.txt','w')
        file.write(str_primes)
        file.close()
        print("The file ‘primes.txt’ was created, and the prime numbers were written into it.")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()