"""
Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return the maximum height of the stacked cuboids.
"""

# dp[i] = largest height if put cuboids[i] at the top

class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:
        cuboids = sorted([sorted(cub) for cub in cuboids], reverse=True)   # sort LxWxH in cube, then sort cube reversely
        ok = lambda x, y: (x[0] >= y[0] and x[1] >= y[1] and x[2] >= y[2]) # make a lambda function to verify whether y can be put on top of x
        n = len(cuboids)
        dp = [cu[2] for cu in cuboids] #najwieksze wymiary prostokata zgodnie z def funkcji                                    # create dp array
        for i in range(1, n):                                              # iterate over each cube
            for j in range(i):                                             # compare with previous calculated cube
                if ok(cuboids[j], cuboids[i]):                             # update dp[i] if cube[i] can be put on top of cube[j]
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])              # always get the maximum                                         # record the largest value
        return max(dp)

# Given set of 3D boxes, where each box has height, width and length. We have
# unlimited supply of these boxes. Find the maximum height of boxes placement that
# the box going on the top should have strictly less length and width than the
# box on which it is going. Also print how to place the boxes on top of each other
# to get this maximum height.


def possible_rotations(box, rotations):
    i = box[0]
    j = box[1]
    k = box[2]
    rotations.append((max(i, j), min(i, j), k))
    rotations.append((max(i, k), min(i, k), j))
    rotations.append((max(j, k), min(j, k), i))


def print_solution(result, rotations):
    i = len(result)-1
    while i != -1:
        print(rotations[i])
        i = result[i]


def box_stacking(boxes):
    rotations = []
    for i in range(len(boxes)):
        possible_rotations(boxes[i], rotations)
    rotations.sort(key=lambda x: x[0]*x[1],reverse=True)
    # rotations.reverse()
    max_height = [-1]*len(rotations)
    result = [0]*len(rotations)
    for i in range(len(max_height)):
        max_height[i] = rotations[i][2]
    for i in range(len(result)):
        result[i] = i
    result[0] = -1
    j = 0
    i = 1
    while j < len(max_height)-1:
        if i == j:
            j = 0
            i += 1
        elif rotations[i][0] < rotations[j][0] \
                and rotations[i][1] < rotations[j][1]:
            height = max_height[j] + rotations[i][2]
            if height > max_height[i]:
                max_height[i] = height
                result[i] = j
            j += 1
        else:
            j += 1
    print_solution(result, rotations)
    return max_height[-1]


boxes = [(1, 2, 4), (3, 2, 5), (3, 4, 9), (3, 2, 7)]
# (height, width, length)
print(box_stacking(boxes))