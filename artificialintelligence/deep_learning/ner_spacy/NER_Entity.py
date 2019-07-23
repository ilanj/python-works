import spacy

nlp = spacy.load("en_core_web_sm")


class Ner():
    def dataset1(self):
        # path = "C://Users//auxouser//Desktop//60h//FIRST_LEVEL//classifydata//dataset_5classes//tech//"
        # filename = "008.txt"
        # f = open(path + filename)
        # text = f.read()
        text="my name is deddd and i am from Google in india"
        return text
        # doc = nlp(u"Smith is Driving this Weekend From Newyork to Newjersy covering 176 Kilometres for a Vacation")


    def aadhar(self):
        nlp = spacy.load("en_core_web_sm")
        path = "C://Users//auxouser//Desktop//60h//FIRST_LEVEL//classifydata//dataset_5classes//tech//"
        filename = "aadar card ilan.txt"
        f = open(path + filename,encoding='utf8')
        text = f.read()
        return text

    def find_entities(self,type):
        if type in "aadhar":
            text=Ner.aadhar(self)
        elif type in "dataset1":
            text=Ner.dataset1(self)
        doc = nlp(text)
        for ent in doc.ents:
            # print(ent.text, ent.start_char, ent.end_char, ent.label_)
            print(ent.text, "->", ent.label_)

if __name__=='__main__':
    obj=Ner()
    aadhar_dataset="aadhar"
    dataset="dataset1"
    obj.find_entities(dataset)