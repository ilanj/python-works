#100-s, >90-A, >80-B, >70-c, >60-D, >50-E, <50-fail
marks=int(input("enter marks"))

if marks>100 or marks<0:
    print("invalid marks.. mark cannot be beyond 100 or within 0")
elif marks==100:
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