import re

def eval(entry: str) -> int:
    entry_total = 0
    f, s = entry.split("-")
    first = int(f)
    second = int(s)
    for x in range(first, second+1):
        num = str(x)
        match = re.search(r"^(\d+)\1$", num)
        if match:
            print(f"Adding {num} to total")
            entry_total += int(num)
    return(entry_total)
        

def main():
    result = 0
    with open("full.txt", "r") as file:
        for line in file.readlines():
            for entry in line.split(","):
                result += eval(entry)
    print(f"Total: {result}")

if __name__ == "__main__":
    main()

