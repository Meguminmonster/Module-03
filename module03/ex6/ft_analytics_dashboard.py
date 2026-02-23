def ft_analytics_dashboard() -> None:
    """Ultimate Analytics Dashboard using Python comprehensions."""
    print("=== Game Analytics Dashboard ===")

    # Datos de entrada
    players = ['alice', 'bob', 'charlie', 'diana']
    scores = [2300, 1800, 2150, 2000]
    # Lista de tuplas (jugador, cantidad_logros) para el Dict Comprehension
    ach_data = [('alice', 5), ('bob', 3), ('charlie', 7), ('diana', 4)]
    raw_regions = ['north', 'east', 'north', 'central', 'east', 'north']

    print("\n=== List Comprehension Examples ===")
    # Filtrar jugadores con más de 2000 puntos
    high_scorers = [
        players[i] for i in range(len(players))
        if scores[i] >= 2000
     ]
    print(f"High scorers (>2000): {high_scorers}")

    # Transformación: doblar puntuaciones altas
    scores_doubled = [s * 2 for s in scores if s > 1500]
    print(f"Scores doubled: {scores_doubled}")

    # Filtrado simple
    active = [p for p in players if p != 'diana']
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    # Mapeo de Puntuaciones
    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print(f"Player scores: {player_scores}")

    # Categorización (Conteo basado en condiciones)
    categories = {
        'high': len([s for s in scores if s >= 2000]),
        'medium': len([s for s in scores if 1000 <= s < 2000]),
        'low': len([s for s in scores if s < 1000])
    }
    print(f"Score categories: {categories}")

    # Conteo de Logros (Dict comprehension desde lista de tuplas)
    achievement_counts = {name: count for name, count in ach_data}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    # Deduplicación de regiones
    active_regions = {r for r in raw_regions}
    print(f"Active regions: {active_regions}")

    # Jugadores únicos (útil si la lista original tuviera duplicados)
    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    print("\n=== Combined Analysis ===")
    # Cálculo de promedio usando LaTeX para la lógica interna:
    # $Average = \frac{\sum scores}{n}$
    avg_score = sum(scores) / len(scores)

    # Encontrar al Top Performer usando max() y el diccionario
    top_p = max(player_scores, key=player_scores.get)
    top_s = player_scores[top_p]
    top_a = achievement_counts.get(top_p, 0)

    print(f"Total players: {len(players)}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_p} ({top_s} points, {top_a} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
