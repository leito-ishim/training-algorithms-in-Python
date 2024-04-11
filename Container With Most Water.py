# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


def get_area(i1, i2, h1, h2):
    wight = abs(i2 - i1)
    area = h1 * wight if h1 < h2 else h2 * wight
    return area

def maxArea(height):
    start_pos = 0
    end_pos = len(height) -1
    max_area = 0
    while start_pos < end_pos:
        max_area = max(max_area, get_area(start_pos, end_pos, height[start_pos], height[end_pos]))
        if height[start_pos] < height[end_pos]:
            start_pos += 1
        else:
            end_pos -= 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
