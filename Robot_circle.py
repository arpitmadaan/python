instructions = "GGL"
direction = [0,1]
position = [0,0]
for _ in range(4):    
    for move in instructions:
        if move == 'G':
            position = [p + d for p, d in zip(position, direction)]
        elif move == 'L':
            direction = [-direction[1], direction[0]]
        elif move == 'R':
            direction = [direction[1], -direction[0]]
if position == [0,0]:
    print(True)
else:
    print(False)
print(f"Updated position: {position}")
# In this problem you can apply any one of below two logics fo rreturn to origin:
#  if position == [0,0] or direction != [0,1]:
# or 
# for _ in range(4): 

# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:

# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.