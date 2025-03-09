from abc import ABC, abstractmethod


class BaseEx(ABC):
    @abstractmethod
    def roi(self):
        pass


class IndianBank(BaseEx):
    def roi(self):
        return 10.58


class SBI(BaseEx):
    def roi(self):
        return 10.99


obj = SBI()
print(obj.roi())
