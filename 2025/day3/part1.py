import sys
import time
from typing import List


TOTAL_NUMS = 2

class Occurence:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index: List[int] = [index]
    
    def add_index(self, index: int):
        self.index.append(index)
    
    def __repr__(self):
        return f"Occurence(value={self.value}, index={self.index})"

class Node:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index
    
    def __repr__(self):
        return f"Node(value={self.value}, index={self.index})"

def eval(line: str) -> int:
    nums = []
    occurences = []
    for x in range(len(line)):
        nums.append(Node(int(line[x]), x))
        found = False
        for occurence in occurences:
            if int(line[x]) == occurence.value:
                occurence.add_index(x)
                found = True
                break
        if not found:
            occurences.append(Occurence(int(line[x]), x))
    
    # Sort by occurrence count (lowest first = least frequent)
    occurences.sort(key=lambda o: len(o.index))
    
    # Take the TOTAL_NUMS least frequent
    least_frequent = occurences[:TOTAL_NUMS]
    
    # Order by first appearance (first index)
    least_frequent.sort(key=lambda o: o.index[0])
    
    # Build the result number
    result = int(''.join(str(o.value) for o in least_frequent))
    
    for occ in least_frequent:
        print(occ)
    print(f"Result: {result}")
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python day3/part1.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    result = 0
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            result += eval(line)
    print(result)

if __name__ == "__main__":
    start_perf = time.perf_counter()
    main()
    end_perf = time.perf_counter()
    print(f"Execution time: {end_perf - start_perf:.4f} seconds")
