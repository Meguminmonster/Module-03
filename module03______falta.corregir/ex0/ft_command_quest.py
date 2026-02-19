import sys


def ft_command_quest() -> None:
    """Process and print arguments passed through terminal."""
    print("=== Command Quest ===\n")
    args = sys.argv

    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")

    print(f"Program name: {args[0]}")
    print(f"Total arguments: {len(args)}\n")


if __name__ == "__main__":
    ft_command_quest()
