totals = []
current = 0

with open("input.txt","r") as file:
    line = file.readline()
    while line:
        if line == "\n":
            totals.append(current)
            current = 0
        else:
            current += int(line)
        line = file.readline()

totals.sort()

print(sum(totals[len(totals) - 3:]))