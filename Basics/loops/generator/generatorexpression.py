print(sum(i*i for i in range(11)))

x=[1,2,3]
y=[5,5,5]
table=[]
table=list(a*b for a,b in zip(x,y))
print(table)