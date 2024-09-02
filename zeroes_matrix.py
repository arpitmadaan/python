# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5],[2,3,5,6]]
col_len = len(matrix)
row_len = len(matrix[0])
zero_positions = []
for i in range(col_len):
    for j in range(row_len):
        if matrix[i][j] == 0:
            zero_positions.append((i,j))
            
for i,j in zero_positions:
    for a in range(col_len):
        matrix[a][j] = 0
    for b in range(row_len):
        matrix[i][b] = 0   
print(matrix)