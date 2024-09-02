# text = "   fly me   to   the moon  "
text = "a"
stripped_reversed = text.rstrip(" ")[::-1]
index = stripped_reversed.find(" ")
if index == -1:
    print(len(stripped_reversed))
else:
    print(index)