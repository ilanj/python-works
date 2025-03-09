"""
String data in a DAWG may take 200x less memory than in a standard Python dict and the raw lookup speed is comparable;
it also provides fast advanced methods like prefix search.
"""

import dawg

words = ["foo", "bar", "foobar", "foö", "bör", "dog", "cat"]
base_dawg = dawg.DAWG(words)
completion_dawg = dawg.CompletionDAWG(words)

print("foo" in base_dawg)
print("dog1" in base_dawg)
print(completion_dawg.has_keys_with_prefix("f"))
print(base_dawg.prefixes("foobarz"))
# print(completion_dawg.has(u'f'))
