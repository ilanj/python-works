n=eval(input("enter any no"))
sum=0
while n!=0:
    rem=(n%10)
    sum=sum+rem
    n=(n//10)#//-does a floor division where 0.9 becomes 0
print(sum)