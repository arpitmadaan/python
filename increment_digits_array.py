digits = [4,3,2,1]
# Output: [4,3,2,2]
number = int(''.join(map(str,digits))) + 1
result = [int(digit) for digit in str(number)]
print(result)
