def print_data(a,*b):
    print('a=',a)
    print('b=',b)

print_data('sd','dd','dded',56)

def print_values(x,**y):
    print('x=',x)
    print('y=',y)
c={'name':'ila','age':25,'place':'chennai'}
print_values('apple',**c)