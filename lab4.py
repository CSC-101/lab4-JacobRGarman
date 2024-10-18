import math
from data import Point  # Import the Point class

# Write your functions for each part in the space below.

# Part 1
def first_element(lst: list[list[int]]) -> list[int]:
    # Filter out empty lists and extract the first element from the rest
    return [sublist[0] for sublist in lst if sublist]

# Part 2
def x_coordinates(points: list[Point]) -> list[float]:
    # Extract the x-coordinate from each point
    return [point.x for point in points]

# Part 3
def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    # Return only points where both x and y coordinates are positive
    return [point for point in points if point.x > 0 and point.y > 0]

# Part 4
import math

def distance(p1: Point, p2: Point) -> float:
    # Calculate Euclidean distance
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# Part 5
def manhattan_distance(p1: Point, p2: Point) -> float:
    # Calculate Manhattan distance
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)

# Part 6
def distance_all(points: list[Point]) -> list[float]:
    origin = Point(0, 0)
    return [distance(origin, point) for point in points]
