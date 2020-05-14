import re


class Aadhar():
    def load_text(self):
        path = "/media/ila/f:/workspace/tesseractocr/io_files/outputfiles/text_from_ocr/"
        filename = "aadar card ilan.txt"
        f = open(path + filename, encoding='utf8')
        text = f.read()
        return text

    def find_pattern(self):
        text=Aadhar.load_text(self)
        aadharno=re.findall("\d+\s+\d+\s+\d\d\d\d",text)
        print("Aadhar no=",aadharno,"  available in ",text)
if __name__=='__main__':
    obj=Aadhar()
    obj.find_pattern()
