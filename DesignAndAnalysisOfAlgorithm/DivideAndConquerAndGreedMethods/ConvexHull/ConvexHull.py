'''
Algorithom

function convexHull(points):
    if len(points) < 3:
        return points

    // Step 1: Find the point with the lowest y-coordinate
    start_point = point with the lowest y-coordinate (and lowest x-coordinate in case of a tie)

    // Step 2: Sort the points by polar angle with respect to the start_point
    sort points by polar angle with respect to start_point

    // Step 3: Initialize a stack and push the first two points onto it
    stack = [points[0], points[1]]

    // Step 4: Iterate over the sorted points
    for i = 2 to len(points) - 1:
        // Step 4a: While the angle formed by the last two points and the current point makes a non-left turn
        while stack has at least two points and orientation of (second-to-last, last, current) is not counterclockwise:
            pop the last point off the stack

        // Step 4b: Push the current point onto the stack
        push current point onto stack

    // Step 5: Return the points remaining on the stack (convex hull)
    return stack
'''

from math import atan2

def orientation(p, q, r):
    """
    Returns the orientation of the triplet (p, q, r).
    Returns:
        0 if p, q, r are collinear
        1 if p, q, r are clockwise
        2 if p, q, r are counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def convex_hull(points):
    if len(points) < 3:
        return points

    # Step 1: Find the point with the lowest y-coordinate
    start_point = min(points, key=lambda p: (p[1], p[0]))

    # Step 2: Sort the points by polar angle with respect to the start_point
    sorted_points = sorted(points, key=lambda p: (atan2(p[1] - start_point[1], p[0] - start_point[0]), p[0], p[1]))

    # Step 3: Initialize a stack and push the first two points onto it
    stack = [sorted_points[0], sorted_points[1]]

    # Step 4: Iterate over the sorted points
    for i in range(2, len(sorted_points)):
        # Step 4a: While the angle formed by the last two points and the current point makes a non-left turn
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()

        # Step 4b: Push the current point onto the stack
        stack.append(sorted_points[i])

    # Step 5: Return the points remaining on the stack (convex hull)
    return stack

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull_points = convex_hull(points)
print("Convex Hull Points:", convex_hull_points)

