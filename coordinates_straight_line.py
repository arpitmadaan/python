# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates = [[0,0],[0,1],[0,-1]]
x0, y0 = coordinates[0]
x1, y1 = coordinates[1]
dx, dy = x1 - x0, y1 - y0
return all(dx * (y - y0) == dy * (x - x0) for x, y in coordinates[1:])

