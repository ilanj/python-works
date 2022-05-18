import glob

files = glob.glob("artificialintelligence/machine_learning/doc_classification/classifydata/dataset_5classes/sport/*")
files = glob.glob("artificialintelligence/machine_learning/doc_classification/classifydata/dataset_5classes/sport/*.txt")
files = glob.glob("artificialintelligence/machine_learning/doc_classification/classifydata/dataset_5classes/sport/data?*.txt")
#to iterate all files from sub folders
files = glob.glob("/home/ila/Documents/repos/python-works/artificialintelligence/machine_learning/doc_classification/classifydata/dataset_5classes/*/*")
files = glob.iglob("/home/ila/Documents/*.txt", recursive=True)
for file in files:
    print(file)
pass

#alternate
import os

# Using os.walk()
for dirpath, dirs, files in os.walk('src'):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if fname.endswith('.c'):
            print(fname)
