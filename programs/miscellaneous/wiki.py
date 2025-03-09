import wikipedia

search = wikipedia.search("tree")
result = wikipedia.page("tree")
print(result.summary)
for link in result.links:
    print(link)
