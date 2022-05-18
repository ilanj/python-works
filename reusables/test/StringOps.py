import enchant
text="This will give you the start position of the word (if it exists, otherwise -1), then you can just " \
         "add the length of the word to it in order to get the index of its end."

class StringOps:


    def start_end_pos(self):
        word='will give'
        start_index = text.find(word)
        end_index = start_index + len(word)
        print(start_index, end_index)

    def remove_specialchars(self, word):
        word= word.strip()
        length= len(word)
        if word[length-1] is not r'\w':
            word= word.replace(word[length-1],'')
        return word

    def dictionary_words(self):
        d = enchant.Dict("en_US")
        f=open('/home/ila/Documents/02.txt')
        text=f.read()
        words=text.split()
        for word in words:
            word= StringOps.remove_specialchars(self, word)
            status = d.check(word)
            print(word, status)


if __name__=='__main__':
    run=StringOps()
    run.dictionary_words()
