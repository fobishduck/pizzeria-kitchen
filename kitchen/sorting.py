"""Putting the kitchen's orders in order."""

from kitchen.orders import Order


def selection_sort_by_total(orders: list[Order]) -> tuple[list[Order], int]:
    """O(n^2). Returns (a new list sorted by total_cents, comparisons made)."""
    remaining = list(orders)
    result: list[Order] = []
    comparisons = 0
    while remaining:
        smallest = 0
        for i in range(1, len(remaining)):
            comparisons += 1
            if remaining[i].total_cents < remaining[smallest].total_cents:
                smallest = i
        result.append(remaining.pop(smallest))
    return result, comparisons
