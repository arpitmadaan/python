text = "the dog is 1 but the dog is bigger than the rat"
number = 2
count = {}
# part to show how to iterate over keys
for word in text.split(' '):
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
for key,value in count.items():
    if value == number:
        print(key,value)
# second part of problem to show how to iterate over values
if number in count.values():
    print("True")
else: 
    print("False")