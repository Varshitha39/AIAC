import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Generate random sensor coordinates
def generate_sensors(n, seed=42):
    random.seed(seed)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Calculate total path distance
def total_distance(path, coords):
    dist = 0
    for i in range(len(path)):
        x1, y1 = coords[path[i]]
        x2, y2 = coords[path[(i + 1) % len(path)]]
        dist += math.hypot(x2 - x1, y2 - y1)
    return dist

# Greedy algorithm
def greedy_path(coords):
    n = len(coords)
    unvisited = set(range(n))
    path = [0]
    unvisited.remove(0)

    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda i: math.hypot(coords[i][0] - coords[last][0], coords[i][1] - coords[last][1]))
        path.append(next_city)
        unvisited.remove(next_city)
    return path

# Simulated Annealing
def simulated_annealing(coords, initial_path, T=1000, cooling_rate=0.995, iterations=10000):
    current_path = initial_path[:]
    best_path = current_path[:]
    best_dist = total_distance(best_path, coords)

    for _ in range(iterations):
        i, j = sorted(random.sample(range(len(coords)), 2))
        new_path = current_path[:]
        new_path[i:j] = reversed(new_path[i:j])
        new_dist = total_distance(new_path, coords)

        if new_dist < best_dist or random.random() < math.exp((best_dist - new_dist) / T):
            current_path = new_path
            if new_dist < best_dist:
                best_path = new_path
                best_dist = new_dist
        T *= cooling_rate
    return best_path

# Plotting function
def plot_path(coords, path, title, color):
    x = [coords[i][0] for i in path + [path[0]]]
    y = [coords[i][1] for i in path + [path[0]]]
    plt.plot(x, y, marker='o', color=color, label=title)
    plt.title("AUV Route Optimization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

# Main execution
if _name_ == "_main_":
    num_sensors = 20
    coords = generate_sensors(num_sensors)

    # Random path
    random_path = list(range(num_sensors))
    random.shuffle(random_path)

    # Greedy path
    greedy = greedy_path(coords)

    # SA optimized path
    sa_path = simulated_annealing(coords, greedy)

    # Distances
    print("Random Path Distance:", total_distance(random_path, coords))
    print("Greedy Path Distance:", total_distance(greedy, coords))
    print("SA Optimized Distance:", total_distance(sa_path, coords))

    # Plotting
    plt.figure(figsize=(10, 6))
    plot_path(coords, random_path, "Random", "gray")
    plot_path(coords, greedy, "Greedy", "blue")
    plot_path(coords, sa_path, "Simulated Annealing", "green")
    plt.grid(True)
    plt.show()