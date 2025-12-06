import sys
import time
from typing import List, Tuple

def is_roll_allowed(map: dict, i: int, j: int) -> bool:
    return map[i, j] == "@" and is_valid_roll(map, i, j)

def is_valid_roll(map: dict, i: int, j: int) -> bool:
    count = 0
    for adj in get_adjacent(i, j):
        if adj in map and map[adj] == "@":
            count += 1
    return count <= 3

def get_num_cols(lines: List[str]) -> int:
    return len(lines[0].strip())

def get_num_rows(lines: List[str]) -> int:
    return len(lines)

def get_adjacent(i: int, j: int) -> List[Tuple[int, int]]:
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]

def print_map(map: dict, cols: int, rows: int):
    for y in range(rows):
        for x in range(cols):
            print(map[x, y], end="")
        print()

def eval(lines: str) -> int:
    # Build a map of the lines
    map = {}
    for y, line in enumerate(lines):
        if line.strip():
            for x, char in enumerate(line.strip()):
                map[x, y] = char
    i, j = 0, 0

    # Tracks the number of rolls not surrounded by more than 4 @s
    total_rolls_removed = 0
    curr_rolls_removed = 1
    removable = set()
    while curr_rolls_removed > 0:
        curr_rolls_removed = 0
        i, j = 0, 0
        while i < get_num_cols(lines):
            while j < get_num_rows(lines):
                if map[i, j] == "." or map[i, j] == "x":
                    map[i, j] = "."
                    j += 1
                    continue
                if is_roll_allowed(map, i, j):
                    curr_rolls_removed += 1
                    total_rolls_removed += 1
                    removable.add((i, j))
                j += 1
            i += 1
            j = 0
        for (i, j) in removable:
            map[i, j] = "x"
        removable.clear()
    return total_rolls_removed

def main():
    if len(sys.argv) != 2:
        print("Usage: python day4/part1.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    result = 0
    with open(input_file, "r") as file:
        lines = file.readlines()
        result += eval(lines)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    start_perf = time.perf_counter()
    main()
    end_perf = time.perf_counter()
    print(f"Execution time: {end_perf - start_perf:.4f} seconds")
