import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

def set_sentiment(matcher, doc, i, matches):
    doc.sentiment += 0.1

pattern1 = [{"ORTH": "Google"}, {"ORTH": "I"}, {"ORTH": "/"}, {"ORTH": "O"}]
pattern2 = [[{"ORTH": emoji, "OP": "+"}] for emoji in ["😀", "😂", "🤣", "😍"]]
matcher.add("GoogleIO", None, pattern1)  # Match "Google I/O" or "Google i/o"
matcher.add("HAPPY", set_sentiment, *pattern2)  # Match one or more happy emoji

doc = nlp(u"A text about Google I/O 😀😀😀")
matches = matcher(doc)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(string_id, span.text)
print("Sentiment", doc.sentiment)