import json

f=open("C:\\Users\\auxouser\\Desktop\\test\\ilanchezhian.txt","w")
# f.write("qefefef\n")
# f.write("frfrfrf")
nos=[34,56,78,76]
json.dump(['foo', {'bar': ('baz', None, 1.0, 2)}],f)

f.close()