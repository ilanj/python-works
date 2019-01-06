#lcm
n1=45
n2=96
max=max(n1,n2)
temp=max
count=2
while(1):

    if(max % n1 is 0 and max % n2 is 0):
        lcm=max
        print(lcm)
        break
    max=temp*count
    count+=1