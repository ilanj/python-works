class Test:
    def data_for_a_document(self):
        path = "G://workspace//pythontutorial//artificialintelligence//doc_classification//classifydata//dataset_5classes//politics//"
        filename = "007.txt"
        f = open(path + filename)
        r = f.read()
        test_doc = []
        test_doc.append(r)
        return test_doc

if __name__ == '__main__':
    obj=Test()
    test =obj.data_for_a_document()
    print(type(test))
