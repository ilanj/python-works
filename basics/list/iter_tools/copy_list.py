import itertools

colors = ['red', 'orange', 'yellow', 'green', 'blue']
alpha_colors, beta_colors, test = itertools.tee(colors, 3) #when 3 not specified default 2
for each in alpha_colors:
    print(each)
print('..')
for each in beta_colors:
     print(each)
print('..')
for each in test:
     print(each)