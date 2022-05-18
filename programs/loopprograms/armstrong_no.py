#153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

n=int(input("enter any no"))
check_n=n
armstrong=0
<<<<<<< HEAD
while n != 0:
=======
while n is not 0:
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
    rem=n % 10
    n = n // 10
    armstrong=armstrong+(rem**3)

<<<<<<< HEAD
if(check_n == armstrong):
=======
if(check_n is armstrong):
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
    print("armstrong no")
else:
    print(" not an armstrong no")
