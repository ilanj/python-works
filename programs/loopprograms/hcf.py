#lcm
n1=876
n2=87
min_element=min(n1, n2)
for no in range(min_element + 1,1,-1):

    if(n1 % no == 0 and n2 % no == 0):
        hcf=no
        break

print(hcf)
# print(max(n1, n2,6,4634,3635,63,6356,356,356,356,356,36,36,36356,36,35,63))