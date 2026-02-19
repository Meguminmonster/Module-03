import sys


def ft_inventory_system() -> None:
    """Manage inventory using dictionaries."""
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return

    inv = {}
    for arg in sys.argv[1:]:
        try:
            item, qty_str = arg.split(':')
            qty = int(qty_str)
            inv[item] = inv.get(item, 0) + qty
        except ValueError:
            print(f"Error parsing '{arg}'")

    if not inv:
        return

    total = sum(inv.values())
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inv.keys())}")

    print("\n=== Current Inventory ===")
    for item, qty in inv.items():
        pct = (qty / total) * 100
        print(f"{item}: {qty} units ({pct:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most = max(inv.items(), key=lambda x: x[1])
    least = min(inv.items(), key=lambda x: x[1])
    print(f"Most abundant: {most[0]} ({most[1]} units)")
    print(f"Least abundant: {least[0]} ({least[1]} units)")

    print("\n=== Item Categories ===")
    print(f"Moderate: {{k: v for k, v in inv.items() if v >= 5}}")
    print(f"Scarce: {{k: v for k, v in inv.items() if v < 5}}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inv.keys())}")
    print(f"Dictionary values: {', '.join(map(str, inv.values()))}")


if __name__ == "__main__":
    ft_inventory_system()
