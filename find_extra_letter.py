word1 = "abcd"
word2 = "bccad"
# word2 = "bcrad"
my_list = list(word1)
for letter in list(word2):
    if letter in my_list:
        my_list.remove(letter)
    else:
        print(letter)
