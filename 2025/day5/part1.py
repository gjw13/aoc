import sys
import time
import os
from typing import Tuple, List

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, number: int) -> bool:
        return self.start <= number <= self.end
    
    def __repr__(self):
        return f"Range(start={self.start}, end={self.end})"

def get_file_input(filepath: str) -> Tuple[List[Range], List[int]]:
    ranges: List[Range] = []
    ingredients: List[int] = []
    end_of_range = False
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                end_of_range = True
                continue
            if not end_of_range:
                start, end = line.split("-")
                ranges.append(Range(int(start), int(end)))
            else:
                ingredients.append(int(line))
    return ranges, ingredients

def main():
    if len(sys.argv) != 2:
        print("Usage: python day5/part1.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    input_file_path = os.path.join(os.path.dirname(__file__), input_file)
    
    ranges, ingredients = get_file_input(input_file_path)
    total = 0
    for ingredient in ingredients:
        for range in ranges:
            if range.contains(ingredient):
                total += 1
                break
    print(f"Total: {total}")

if __name__ == "__main__":
    start_perf = time.perf_counter()
    main()
    end_perf = time.perf_counter()
    print(f"Execution time: {end_perf - start_perf:.4f} seconds")
