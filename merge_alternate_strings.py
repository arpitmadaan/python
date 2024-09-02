word1 = "abcd"
word2 = "pq"
result = []
i = 0
while i < len(word1) or i < len(word2):
    if i < len(word1):
        result.append(word1[i])
    if i < len(word2):
        result.append(word2[i])
    i += 1
print(''.join(result))