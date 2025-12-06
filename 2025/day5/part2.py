import sys
import time
import os
from typing import List

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    def contains(self, number: int) -> bool:
        return self.start <= number <= self.end
    def overlaps(self, other: 'Range') -> bool:
        return (self.contains(other.start) or self.contains(other.end) or 
                other.contains(self.start) or other.contains(self.end))

    def __repr__(self):
        return f"Range(start={self.start}, end={self.end})"

def get_file_input(filepath: str) -> List[Range]:
    ranges: List[Range] = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            start, end = line.split("-")
            ranges.append(Range(int(start), int(end)))
    return ranges

def merge_ranges(ranges: List[Range]) -> List[Range]:
    i = 0
    while i < len(ranges):
        j = i + 1
        while j < len(ranges):
            if ranges[i].overlaps(ranges[j]):
                # Merge j into i, then remove j
                ranges[i] = Range(min(ranges[i].start, ranges[j].start), max(ranges[i].end, ranges[j].end))
                ranges.pop(j)
                # Reset j to check all remaining ranges against the newly merged range
                j = i + 1
            else:
                j += 1
        i += 1
    return ranges

def main():
    if len(sys.argv) != 2:
        print("Usage: python day5/part2.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    input_file_path = os.path.join(os.path.dirname(__file__), input_file)
    
    ranges = get_file_input(input_file_path)
    new_ranges = merge_ranges(ranges)

    total = 0
    for range in new_ranges:
        total += range.end - range.start + 1
    print(f"Total: {total}")

if __name__ == "__main__":
    start_perf = time.perf_counter()
    main()
    end_perf = time.perf_counter()
    print(f"Execution time: {end_perf - start_perf:.4f} seconds")
