import random
import string
from collections import OrderedDict

from dataclasses import dataclass

model_list = []

@dataclass
class PatientInformation():
    __slots__ = ['name', 'dob']
    name : str
    dob : str

class Access():

    def access_data(self):

        for i in range(10):
            name=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            dob=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            obj = PatientInformation(name, dob)
            model_list.append(obj)
        print(model_list)
        for each in model_list:
            print(each.name, each.dob)

run= Access()
run.access_data()






