text = "Arpit Madaaan"
low = text.lower()
count = {}
for letter in low:
    if letter != ' ':
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

for key,value in count.items():
    print(key,value)