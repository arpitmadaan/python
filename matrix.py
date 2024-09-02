mat = [[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
pdsum = 0
sdsum = 0
for i in range(n):
    pdsum += mat[i][i]
    sdsum += mat[i][n-i-1]
if n%2 == 0:
    pass
else:
    sdsum -= mat[n//2][n//2]
print(pdsum+sdsum)