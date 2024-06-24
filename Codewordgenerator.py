code = input("Enter Your code word: ")
words = code.split(" ")
coding = input("1 for coding or 0 for Decoding: ")
coding = True if (coding == "1") else False
print(coding)
if coding:
    nword = []
    for word in words:
        if len(code) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            codenew = r1 + code[1:] + code[0] + r2
            nword.append(codenew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
else:
    nword = []
    for word in words:
        if len(word) >= 6 and word.startswith("dsf") and word.endswith("jkr"):
            decoded_word = word[-1] + word[3:-4] + word[-4]
            nword.append(decoded_word)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))

