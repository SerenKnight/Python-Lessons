def word_rennips():
    rennip = []
    words = input("\nPlease input one or more words: \n\n")
    word_list = words.split(" ")
    for word in word_list:
        if len(word) >= 5:
            word = word[::-1]
            rennip.append(word)
        else:
            rennip.append(word)
    print("\n" + " ".join(e for e in rennip))


word_rennips()
