'''
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
'''
def read_data():
    f = open("G:\workspace\pythontutorial\print2console.txt")
    r = f.read()
    print(r)
    f.close()

def append_data():
    f = open("G:\workspace\pythontutorial\print2console.txt","a")
    f.write("am new line added")
    f.close()

def write_data():
    f=open("sample.txt","w")
    f.write("just writing a sample data to file")
    f.close()
    f=open("sample.txt")
    print(f.read())

if __name__ == "__main__":
    # read_data()
    # append_data()
    # read_data()
    write_data()
