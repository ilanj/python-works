student =	{
  "name": "ila",
  "place": "chennai",
  "id": 36,
    12:25,
    14:"sddd"
}
print(student)
str=student[12]
print(str)
str=student.get("place")
print(str)
student["place"]="shozhinganallur"
print(student)
student["college"]="aiht"

for x,y in student.items():
    print(x,y)

if "id" in student:
  print(student.get("id"), ' is available')

print(student)
student.pop(14)
print(student)
x = ('key1', 'key2', 'key3')
y="fff","ded","fgg"
thisdict = dict.fromkeys(x,y)
print(thisdict)