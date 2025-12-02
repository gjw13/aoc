

if __name__ == "__main__":
    with open("full.txt") as f:
        lines = f.readlines()

    total = 0
    max_total = 0
    left, right = [], []

    for line in lines:
        line = line.strip().split("   ")
        left.append(line[0])
        right.append(line[1])
    
    for l, r in zip(sorted(left), sorted(right)):
        total += abs(int(l) - int(r))
    print(total)
