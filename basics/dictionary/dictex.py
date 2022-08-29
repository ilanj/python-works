"""
dict example:
1. dictname.popitem() deletes last element from the dict
2. same as pop, del dictname["key"]
3. dictname.pop("key") removes a particular entry
"""
student =	{
  "name": "ila",
  "place": "chennai",
  "id": 36,
    12:25,
    14:"sddd"
}
print(student)
studname=student["name"]
print(studname)

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
student.popitem() #college as last key is removed
print("after pop",student)
student.pop(12) #key 12 is removed
del student["place"] # similar to pop
print(student)

