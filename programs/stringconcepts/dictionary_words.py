"""
brew install enchant
"""
import re
import enchant

text = (
    "This will give you the start position of the word (if it exists, otherwise -1), then you can just "
    "add the length of the word to it in order to get the index of its end."
)


class StringOps:

    def start_end_pos(self):
        word = "will give"
        start_index = text.find(word)
        end_index = start_index + len(word)
        print(start_index, end_index)

    def dictionary_words(self):
        d = enchant.Dict("en_US")
        status = d.check("NICOLE")
        print(status)
        # f=open('')
        # text=f.read()
        # words=text.split()
        # for word in words:
        #     # word= StringOps.remove_specialchars(self, word)
        #     status = d.check(word)
        #     print(word, status)

    def check_dictionary_word(self, word):
        name = word
        words = []
        # word= re.sub('[^a-zA-Z]', ' ', word)
        # word= re.sub(' +',' ', word)
        words = word.split()
        dict = enchant.Dict("en_US")
        check_word = words[-1]
        status = dict.check(check_word)
        if status:
            word = word.replace(check_word, "")
            print(name, "----------", word)
        return status


if __name__ == "__main__":
    run = StringOps()
    run.dictionary_words()
    # with open("/home/ila/Documents/abbyy/patientnames.txt") as fptr:
    #     names= fptr.readlines()
    # for each in names:
    #     each= each.strip()
    #     run.check_dictionary_word(each)
