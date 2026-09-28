def normalize_label(value):
    label = value.strip()
    if not label:
        raise ValueError("label must not be empty")
    return label
