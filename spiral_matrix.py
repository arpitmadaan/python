matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
total = len(matrix)*len(matrix[0])
result = []
# for item in matrix[0]:
for i in range(len(matrix[0])):
    result.append(matrix[0][i])
for i in range (1,len(matrix)):
    result.append(matrix[i][len(matrix)])
for i in range(len(matrix[0])-2, -1, -1):
    result.append(matrix[len(matrix)-1][i])


print(result)