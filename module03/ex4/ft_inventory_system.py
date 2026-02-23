import sys


def ft_inventory_system() -> None:
    """Manage inventory using dictionaries and nested structures."""
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return

    # Usaremos una estructura anidada como pide el ejercicio:
    # inv = {"sword": {"qty": 1}, "potion": {"qty": 5}}
    inv = {}

    for arg in sys.argv[1:]:
        try:
            item_name, qty_str = arg.split(':')
            qty = int(qty_str)

            if item_name in inv:
                # Usando update() como pide el ejercicio
                new_qty = inv[item_name]['qty'] + qty
                inv[item_name].update({'qty': new_qty})
            else:
                inv[item_name] = {'qty': qty}
        except ValueError:
            print(f"Error parsing '{arg}'")

    if not inv:
        return

    # Cálculos iniciales
    total_qty = sum(item['qty'] for item in inv.values())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_qty}")
    print(f"Unique item types: {len(inv.keys())}")

    print("\n=== Current Inventory ===")
    # Ordenar por cantidad (descendente)
    sorted_inv = sorted(inv.items(), key=lambda x: x[1]['qty'], reverse=True)
    for name, data in sorted_inv:
        qty = data['qty']
        pct = (qty / total_qty) * 100
        unit_str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_str} ({pct:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most = max(inv.items(), key=lambda x: x[1]['qty'])
    least = min(inv.items(), key=lambda x: x[1]['qty'])
    print(f"Most abundant: {most[0]} ({most[1]['qty']} units)")
    print(f"Least abundant: {least[0]} ({least[1]['qty']} units)")

    print("\n=== Item Categories ===")
    moderate = {k: v['qty'] for k, v in inv.items() if v['qty'] >= 5}
    scarce = {k: v['qty'] for k, v in inv.items() if v['qty'] < 5}
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    # Identificar ítems con solo 1 unidad
    needs_restock = [k for k, v in inv.items() if v['qty'] == 1]
    print(f"Restock needed: {', '.join(needs_restock)}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inv.keys())}")
    inv_values = [str(inv[k].get('qty')) for k in inv]
    print(f"Dictionary values: {', '.join(inv_values)}")
    has_sword = 'sword' in inv
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


if __name__ == "__main__":
    ft_inventory_system()
