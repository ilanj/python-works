student =	{
  "name": "ila",
  "place": "chennai",
  "id": 36,
    12:25,
    14:"sddd"
}
print(student)
name=student["name"]
print(name)

str=student.get("place")
print(str)
student["place"]="shozhinganallur"
print(student)
student["college"]="aiht"
print(student)

for x,y in student.items():
    print(x,y)

if "id" in student:
  print(student.get("id"), ' is available')

print(student)
student.popitem()
print("after pop",student)
student.pop(12)
print(student)

