import sys


def analyze_scores() -> None:
    """Analiza una lista de puntuaciones dadas por argumentos."""
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2>")
        return

    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score, skipping.")

    if not scores:
        print("No valid scores to analyze.")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    analyze_scores()
