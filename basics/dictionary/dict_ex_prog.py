import json
import pprint

student={
    "name":"bala",
    "id":36,
    43:"check",
    "address":"navalur"
}

print(student)
pprint.pprint(student)
student_asjson=json.dumps(student)
print(student_asjson)
for x,y in student.items():
<<<<<<< HEAD
    print(f"{x} -> {y}")
=======
    print(x,"\t",y)
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2

