from typing import Generator


def game_stream(limit: int) -> Generator[dict, None, None]:
    """Generator that produces events on demand."""
    players = ['alice', 'bob', 'charlie']
    events = ['killed monster', 'found treasure', 'leveled up']

    for i in range(1, limit + 1):
        yield {
            'id': i,
            'player': players[i % len(players)],
            'level': (i % 20) + 1,
            'action': events[i % len(events)]
        }


def ft_data_stream() -> None:
    """Process a simulated infinite stream using generators."""
    print("=== Game Data Stream Processor ===\n")
    total_events = 1000
    print(f"Processing {total_events} game events...\n")

    high_level = 0
    treasure = 0
    level_up = 0

    for event in game_stream(total_events):
        if event['id'] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

        if event['level'] >= 10:
            high_level += 1
        if event['action'] == 'found treasure':
            treasure += 1
        elif event['action'] == 'leveled up':
            level_up += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("Memory usage: Constant (streaming)")


if __name__ == "__main__":
    ft_data_stream()
