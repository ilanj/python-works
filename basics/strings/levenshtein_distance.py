# reference https://pypi.org/project/fuzzywuzzy/
#requirement pip install fuzzywuzzy

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))

print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))

print(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
print(process.extract("new york jets", choices, limit=2))
