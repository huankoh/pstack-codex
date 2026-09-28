from labels import normalize_label
from limits import allocate_units


def render_usage(label, requested, cap):
    return f"{normalize_label(label)}: {allocate_units(requested, cap)}"
