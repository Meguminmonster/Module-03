import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    """Calculates the 3D Euclidean distance between two points."""
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def parse_coord(coord_str: str) -> tuple | None:
    """Converts a string 'x,y,z' to a tuple of integers"""
    try:
        parts = coord_str.split(',')
        if len(parts) != 3:
            raise ValueError("Needs 3 dimensions (x,y,z)")
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    pos1 = (10, 20, 5)

    print(f"Position created: {pos1}")
    dist1 = round(calculate_distance(origin, pos1), 2)
    print(f"Distance between {origin} and {pos1}: {dist1}\n")

    arg_valid = "3,4,0"
    print(f'Parsing coordinates: "{arg_valid}"')
    pos2 = parse_coord(arg_valid)
    if pos2:
        print(f"Parsed position: {pos2}")
        dist2 = round(calculate_distance(origin, pos2), 2)
        print(f"Distance between {origin} and {pos2}: {dist2}")

    arg_invalid = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{arg_invalid}"')
    parse_coord(arg_invalid)

    print("\nUnpacking demonstration:")
    if pos2:
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
