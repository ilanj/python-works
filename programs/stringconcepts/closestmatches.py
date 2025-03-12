from difflib import get_close_matches

def closeMatches(word, patterns):
    print(get_close_matches(word, patterns))

# Driver program
if __name__ == "__main__":
    word = "ilanohe2hia"
    patterns = ["ilanchezhian", "sudharsan:", "mahendiran", "suresh kumae"]
    closeMatches(word, patterns)
