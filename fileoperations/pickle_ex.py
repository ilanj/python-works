# Python3 program to illustrate store
# efficiently using pickle module
# Module translates an in-memory Python object
# into a serialized byte stream—a string of
# bytes that can be written to any file-like object.

import pickle


def storeData():
    # initializing data to be stored in db
    Omkar = {"key": "Omkar", "name": "Omkar Pathak", "age": 21, "pay": 40000}
    Jagdish = {"key": "Jagdish", "name": "Jagdish Pathak", "age": 50, "pay": 50000}

    # database
    db = {}
    db["Omkar"] = Omkar
    db["Jagdish"] = Jagdish

    # Its important to use binary mode
    dbfile = open("examplePickle", "ab")

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()


def loadData():
    # for reading also binary mode is important
    dbfile = open("examplePickle", "rb")
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, "=>", db[keys])
    dbfile.close()


if __name__ == "__main__":
    storeData()
    loadData()
