import re


class Aadhar():
    def load_text(self):
<<<<<<< HEAD
        text = "a nos can be 5845 6524 7859 and to test negative 8745 8956 2562 5625 85"
=======
        path = "/media/ila/f:/workspace/tesseractocr/io_files/outputfiles/text_from_ocr/"
        filename = "aadar card ilan.txt"
        f = open(path + filename, encoding='utf8')
        text = f.read()
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
        return text

    def find_pattern(self):
        text=Aadhar.load_text(self)
<<<<<<< HEAD
        aadharno=re.findall(r"\d{4}\s\d{4}\s\d{4}",text)
=======
        aadharno=re.findall("\d+\s+\d+\s+\d\d\d\d",text)
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
        print("Aadhar no=",aadharno,"  available in ",text)
if __name__=='__main__':
    obj=Aadhar()
    obj.find_pattern()
