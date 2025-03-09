# why strings are immutable (not changable)
print("Strings are  immutable")
f_name = "ilan"
s_name = f_name
f_name = "chezhian"
print("f_name", f_name)
print("s_nme", s_name)

# same above scenario for a list showing lists are mutable
print(" listas are mutable")
list1 = [1, 2, 3, 4]
list2 = list1
list1[1] = "two"
print("list1", list1)
print("list2", list2)

# how can we avoid this using copy
print(" a new list can be mutable using copy")
import copy

list1 = [1, 2, 3, 4]
list2 = copy.deepcopy(list1)
list1[1] = "two"
print("list1", list1)
print("list2", list2)
