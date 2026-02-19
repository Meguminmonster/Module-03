import sys
import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    """Calculates the 3D Euclidean distance between two points."""
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def parse_coord(coord_str: str) -> tuple | None:
    """Converts a string 'x,y,z' to a tuple of floats"""
    try:
        parts = coord_str.split(',')
        if len(parts) != 3:
            raise ValueError("Needs 3 dimensions (x,y,z)")
        return (float(parts[0]), float(parts[1]), float(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details Type: ValueError, Args: {e.args}\n")
        return None


def ft_coordinate_system() -> None:
    """Demonstrate the use of tuples for coordinate systems."""
    print("=== Game Coordinate System ===\n")
    origin = (0.0, 0.0, 0.0)
    pos1 = (10.0, 20.0, 5.0)

    print(f"Position created: {pos1}")
    print(f"Distance between {origin} and {pos1}: "
          f"{calculate_distance(origin, pos1):.2f}")

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(f'\nParsing coordinates: "{arg}"')
            pos = parse_coord(arg)
            if pos:
                print(f"Parsed position: {pos}")
                dist = calculate_distance(origin, pos)
                print(f"Distance between {origin} and {pos}: {dist:.2f}\n")

                # Unpacking demonstration
                x, y, z = pos
                print("Unpacking demonstration:")
                print(f"Player at x={x}, y={y}, z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
