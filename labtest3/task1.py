#!/usr/bin/env python3
import sys

def merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    merged = merge(L, R)
    print(f"Merging {L} and {R} -> {merged}")
    return merged

if __name__ == "__main__":
    s = input("Enter integers separated by spaces or commas: ").strip()
    if not s:
        print("No input provided.")
        sys.exit(0)
    s = s.replace(',', ' ').strip('[]()')
    try:
        arr = [int(x) for x in s.split() if x]
    except ValueError:
        print("Invalid input. Please enter integers only.")
        sys.exit(1)

    result = merge_sort(arr)
    print("Sorted:", result)
