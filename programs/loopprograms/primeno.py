def check_prime_no(n):
    flag=0
    for each in range(2,n//2):
        if(n%each==0):
            flag=1
            break
    if flag == 0:
        print(n," is prime")
        return n
    else:
        print(n," is not prime")

def generate_prime_no(n):
    for each in range(2,n+1):
        flag=0
        for itr in range(2,each):
            if each % itr == 0:
                flag=1
                break
        if flag == 0:
            print(each)


check_prime_no(18)
generate_prime_no(50)
