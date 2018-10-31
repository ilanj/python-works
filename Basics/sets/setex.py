#as set is un ordered u cannot do any operation with index
elements={"aaa",56446,25.36,'vfs'}
print(elements)

elements.add("new_element")
elements.add(45)
#order changes at every execution
print(elements)
elements.pop()
print(elements)

nos={25,89,85}
print(sum(nos))
nos.add(25)
print(nos)
nos.remove(25)
print(nos)
nos.add(98)
print(nos)
nos.pop()
print(nos)

