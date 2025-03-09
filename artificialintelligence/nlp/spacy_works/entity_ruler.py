import os
from spacy.matcher import Matcher, PhraseMatcher
import spacy
from collections import Counter

# This is the testing file
filePath = "input.txt"


def getInputContent(inputFilePath):
    print("**inputFilePath")
    docContent = []
    if os.path.isfile(inputFilePath):
        try:
            file = open(inputFilePath, "r", encoding="utf8")
            docContent = file.read()
            return docContent
        except Exception as err:
            print(err)
    return docContent


def myPhraseMatcher(content):
    nlp = spacy.load("en_core_web_sm")
    phraseMatcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    terms = ["cloud computing", "it", "information"]
    # Only run nlp.make_doc to speed things up
    patterns = [nlp.make_doc(text) for text in terms]
    phraseMatcher.add("Match_By_Phrase", None, *patterns)
    doc = nlp(content)
    matches = phraseMatcher(doc)
    print("phraseMatcher============================")
    matchedTokens = []

    for match_id, start, end in matches:
        span = doc[start:end]
        print(span.text)
        matchedTokens.append(span.text.lower())

    c = Counter(matchedTokens)
    for token, count in c.most_common(3):
        print("%s: %7d" % (token, count))


def myTokenMatcher(content):
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    print("Match_By_Token============================")
    pattern1 = [{"LOWER": "cloud"}, {"LOWER": "computing"}]
    pattern2 = [{"TEXT": "IT"}]
    pattern3 = [{"TEXT": "EDI"}]
    pattern4 = [{"LOWER": "interface"}]

    matcher.add("Match_By_Token", None, pattern1, pattern2, pattern3, pattern4)
    doc = nlp(content)
    matches = matcher(doc)

    matchedTokens = []
    for match_id, start, end in matches:
        span = doc[start:end]
        print(span.text)
        matchedTokens.append(span.text.lower())
    c = Counter(matchedTokens)
    for token, count in c.most_common(3):
        print("%s: %7d" % (token, count))


def main(argv=None):
    # myPhraseMatcher(getInputContent(filePath))
    myTokenMatcher(getInputContent(filePath))


if __name__ == "__main__":
    main()
