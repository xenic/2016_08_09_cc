from helper import clean_word

#filename = "data/the_count_of_monte_cristo.txt"
filename = "data/war_and_peace.txt"
concordance = {}
with open(filename) as f:
    for line in f:
        words = line.split()
        for word in words:
            word = clean_word(word)
            if word in concordance:
                concordance[word] += 1
            else:
                concordance[word] = 1

for word, count in sorted(concordance.items(), key=lambda x:x[1]):
    print(word, count)

while True:
    user_search = input("What word are you intersted in? ")
    if user_search == "":
        exit()
    try:
        print("%s: %s" % (user_search, concordance[user_search]))
    except:
        print("%s did not appear in the book." % user_search)
