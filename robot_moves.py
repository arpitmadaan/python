import sys

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for item in moves:
            if item == 'L':
                y -= 1
            elif item == 'R':
                y += 1
            elif item == 'U':
                x += 1
            elif item == 'D':
                x -= 1
        return x == 0 and y == 0

if __name__ == "__main__":

    moves = sys.argv[1]
    # Create an instance of the Solution class
    solution = Solution()

    # Call the judgeCircle method with the input moves
    result = solution.judgeCircle(moves)
    print(result)

# more easier approach below
# return (ct := Counter(moves))["R"] == ct["L"] and ct["U"] == ct["D"]

# input to be given like
# python .\robot_moves.py UDRLUURRDDLL 