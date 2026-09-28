def allocate_units(requested, cap):
    if requested < 0 or cap < 0:
        raise ValueError("requested units and cap must be nonnegative")
    return min(requested, cap)
