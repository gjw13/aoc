import re

# Compile regex once for efficiency
PATTERN = re.compile(r"^(\d+?)\1+$")

def eval(entry: str) -> int:
    """Find sum of all numbers with repeating pattern in range."""
    entry_total = 0
    first, second = entry.split("-")
    start, end = int(first), int(second)
    
    # We need to check each number, but with compiled regex it's faster
    for x in range(start, end + 1):
        if PATTERN.search(str(x)):
            entry_total += x
    
    return entry_total
        

def main():
    result = 0
    with open("full.txt", "r") as file:
        for line in file:
            for entry in line.split(","):
                result += eval(entry)
    print(f"Total: {result}")

if __name__ == "__main__":
    main()
