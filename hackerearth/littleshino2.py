import math
nos=input()
a,b=nos.split()
a=int(a)
b=int(b)
result=[]

min=a if a < b else b
min_half = min // 2
min_half = math.ceil(min_half)
sqrt_no = math.ceil(math.sqrt(min_half + 1))

while min_half>0:
    if (a%min_half == 0 or b % min_half == 0):
        result.append(min_half)
    min_half = min_half // 2
    min_half = math.ceil(min_half)
    sqrt_no = math.ceil(math.sqrt(min_half + 1))

iter_range=range(1,(sqrt_no+1) )

result1=list(filter(lambda x:(a%x==0 and b%x==0),iter_range))
if(a%b==0 or b%a==0):
    result.append(min)
result=result+result1

print(len(result))
print(result)