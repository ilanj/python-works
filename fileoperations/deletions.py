
import os
def deletefile():
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")

def deletefolder():
    dirname="D:\capture//test-files"
    if os.path.exists(dirname):
        os.rmdir(dirname)
    else:
        print(f" {dirname} dosen't exist")

if __name__== "__main__":
    deletefile()
    deletefolder()

