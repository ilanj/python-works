import json

student={
    "name":"Hajara",
    "id":36,
    43:"check",
    "address":"navalur"
}

print(student)
student_asjson=json.dumps(student)
print(student_asjson)
for x,y in student.items():
    print(x,"\t",y)

