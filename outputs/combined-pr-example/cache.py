def save(cache, key, value, persist):
    if key in cache and cache[key] == value:
        return "unchanged"
    persist(key, value)
    cache[key] = value
    return "written"
