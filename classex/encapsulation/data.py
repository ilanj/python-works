""" accessing a class private data outside is called encapsulation"""
class Data:
    name="ila"
    _id=36
    __location="chennai"
    __role="kkldc"

class AccessData:
    obj=Data()
    obj.name="ila.j"
    print(obj.name)
    obj._id=43
    print(obj._id)
    obj._Data__location="Sozhinganallur" #a kind of encapsi
    print(obj._Data__location)
