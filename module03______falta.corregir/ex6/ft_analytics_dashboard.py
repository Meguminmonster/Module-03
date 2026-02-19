def ft_analytics_dashboard() -> None:
    """Dashboard usando List, Dict y Set comprehensions."""
    print("=== Game Analytics Dashboard ===")

    scores = [1500, 2300, 1800, 2150, 900]
    players = ['alice', 'bob', 'charlie', 'diana', 'eve']
    achievements = ['first_kill', 'level_10', 'first_kill', 'speed_demon']

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p for i, p in enumerate(players) if scores[i] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [s * 2 for s in scores if s > 1500]
    print(f"Scores doubled: {scores_doubled}")

    active = [p for p in players if p != 'eve']
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print(f"Player scores: {player_scores}")

    categories = {
        'high': len([s for s in scores if s >= 2000]),
        'medium': len([s for s in scores if 1000 <= s < 2000]),
        'low': len([s for s in scores if s < 1000])
    }
    print(f"Score categories: {categories}")

    print("\n=== Set Comprehension Examples ===")
    unique_achievements = {a for a in achievements}
    print(f"Unique achievements: {unique_achievements}")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(scores) / len(scores)}")


if __name__ == "__main__":
    ft_analytics_dashboard()
