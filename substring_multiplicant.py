word = "abcabcabcabc"
# word = "abcab"
if word in (word+word)[1:-1]:
    print(True)
else:
    print(False)
