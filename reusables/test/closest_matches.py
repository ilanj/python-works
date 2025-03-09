from difflib import get_close_matches


def print_data(patterns, word):
    print(get_close_matches(word, patterns))


# Driver program
def closest_matches():
    words = "Hi i am ilanchezhian from pondicherry and now in chennai"
    patterns = ["ilanchezhian", "sudharsan:", "mahendiran", "suresh kumae"]
    for word in words.split():
        print_data(patterns, word)


def closest_matches_augmentation():
    patterns = ["284-26-8656"]

    with open(
        "/home/ila/Documents/doccano_text_ip/Referrals/Refferal Form/Refferal Form_0.txt"
    ) as fptr:
        text = fptr.read()
        words = text.split()
        for word in words:
            match = get_close_matches(word, patterns, cutoff=0.9)
            if match:
                print(patterns, word)
                break


if __name__ == "__main__":
    closest_matches_augmentation()
