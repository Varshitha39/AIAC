def find_common(a, b):
    b_set = set(b)
    res = []
    seen = set()
    for item in a:
        if item in b_set and item not in seen:
            res.append(item)
            seen.add(item)
    return res
print(find_common([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
print(find_common(['apple','banana','cherry'],['banana','cherry','date']))
