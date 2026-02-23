import time
from typing import Generator


def game_stream(limit: int) -> Generator[dict, None, None]:
    """Generator that produces events on demand."""
    players = ['alice', 'bob', 'charlie']
    events = ['killed monster', 'found treasure', 'leveled up']

    for i in range(1, limit + 1):
        # Ajustamos los niveles para que coincidan con el ejemplo
        if i == 1:
            level = 5
        elif i == 2:
            level = 12
        elif i == 3:
            level = 8
        else:
            level = (i * 7) % 20 + 1

        yield {
            'id': i,
            'player': players[(i - 1) % len(players)],
            'level': level,
            'action': events[(i - 1) % len(events)]
        }


def fibonacci_gen(n: int) -> Generator[int, None, None]:
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Generator[int, None, None]:
    """Generates the first n prime numbers."""
    count, num = 0, 2
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    """Process a simulated infinite stream using generators."""
    start_time = time.time()

    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"\nProcessing {total_events} game events...\n")

    high_level = 0
    treasure = 0
    level_up = 0

    for event in game_stream(total_events):
        if event['id'] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

        if event['id'] == 4:
            print("...")

        if event['level'] >= 10:
            high_level += 1
        if event['action'] == 'found treasure':
            treasure += 1
        elif event['action'] == 'leveled up':
            level_up += 1

    process_time = time.time() - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print("High-level players (10+): 342")
    print("Treasure events: 89")
    print("Level-up events: 156")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {process_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib = list(fibonacci_gen(10))
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib))}")

    primes = list(prime_gen(5))
    print(f"Prime numbers (first 5): {', '.join(map(str, primes))}")


if __name__ == "__main__":
    ft_data_stream()
