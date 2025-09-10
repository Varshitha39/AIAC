def calculate_average(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    return sum(scores) / len(scores)


def find_highest(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    return max(scores)


def find_lowest(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    return min(scores)


def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
process_scores([10, 20, 30, 40, 50])

