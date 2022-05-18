import re


class Aadhar():
    def load_text(self):
        text = "a nos can be 5845 6524 7859 and to test negative 8745 8956 2562 5625 85"
        return text

    def find_pattern(self):
        text=Aadhar.load_text(self)
        aadharno=re.findall(r"\d{4}\s\d{4}\s\d{4}",text)
        print("Aadhar no=",aadharno,"  available in ",text)
if __name__=='__main__':
    obj=Aadhar()
    obj.find_pattern()
