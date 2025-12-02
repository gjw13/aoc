import time

def main():
    with open("full.txt") as f:
        lines = f.readlines()

    total = 0
    max_total = 0
    left, right = [], []

    for line in lines:
        line = line.strip().split("   ")
        left.append(line[0])
        right.append(line[1])
    
    # create occurence map for right side
    right_map = {}
    for r in right:
        if r in right_map:
            right_map[r] += 1
        else:
            right_map[r] = 1
    for l in left:
        total += int(l) * right_map.get(l, 0)
    print(total)

if __name__ == "__main__":
    start_perf = time.perf_counter()
    main()
    end_perf = time.perf_counter()
    print(f"Execution time: {end_perf - start_perf:.4f} seconds")
