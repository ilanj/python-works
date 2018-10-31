#100-s, >90-A, >80-B, >70-c, >60-D, >50-E, <50-fail
marks=int(input("enter marks"))
if marks<0 or marks>100:
    print("invalid marks")
elif(marks==100):
    print("s grade")
elif marks>90:
    print('A grade')
elif marks > 80:
    print('B grade')
elif marks > 70:
    print('C grade')
elif marks > 60:
    print('D grade')
elif marks > 50:
    print('E grade')
else:
    print("Fail")