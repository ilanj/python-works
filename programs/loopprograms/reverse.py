# sum
n=eval(input("enter any no"))
sum=0
while n!=0:
    rem=(n%10)
    sum=sum+rem
    n=(n//10)#//-does a floor division where 0.9 becomes 0
print(sum)

# reverse
n=eval(input("enter any no"))
rev=0
while n!=0:
    rem=(n%10)
    rev=rev*10 + rem
    n=(n//10)#//-does a floor division where 0.9 becomes 0
print(rev)