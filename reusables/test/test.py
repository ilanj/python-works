import re

def test1():
    f = open("/home/ila/Downloads/text_npi/text_blob/5cc6a0b9bc831709f083aa39/02.txt")
    text = f.read()
    words = text.split()
    for w in words:
        if re.search("^[0-9]{10}$", w):
            print(w)

def test2():
    text= 'hi aaa'
    words=text.split()
    print(words)

def test3():
    pattern = re.compile('^[0-9]{10}$')
    if re.match(r'^[0-9]{10}$','1254789587'):
        print('yes')
    else:
        print('no')

def test4():
    name='0123456789'
    word=slice(2,8)
    print(name[word])

#take every two words
def test5():
    f=open('/home/ila/snap/skype/common/1.txt')
    text=f.read()
    words=text.split()
    for position in range(0,len(words),2):
        c=0
        while c<2:
            if c==0:
                print(words[position],words[position+1])
            c+=1

def test6():
    stuff = ["oranges", "POTATOES", "Pencils", "PAper"]
    print(any(s.lower() == 'paper' for s in stuff))
    print(stuff)

def iterate_files():
    import os
    rootdir = '/home/ila/Downloads/text_for_npi/text_npi_1'

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print("subdir",subdir)
            foldernames=subdir.rsplit('/')[-1]
            print()
            print("dirs",dirs)
            print("files",file)
            print(os.path.join(subdir, file))

def split_string():
    name="1023548.0"
    name=name.split('.')[-1]
    print(name)

def check_empty_string():
    name= ''
    if name:
        print('not rmpty')

check_empty_string()
iterate_files()