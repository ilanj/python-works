class Test:
    def data_for_a_document(self):
        path = "/home/ila/PycharmProjects/pythonworks/artificialintelligence/machine_learning/doc_classification/classifydata/dataset_5classes/entertainment/"
        filename = "009.txt"
        f = open(path + filename)
        r = f.read()
        test_doc = []
        test_doc.append(r)
        return test_doc

if __name__ == '__main__':
    obj=Test()
    test =obj.data_for_a_document()
    print(type(test))
