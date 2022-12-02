
score = 0
values = {"A": 1, "B": 2, "C":3}
to_win = [2,3,1]
to_lose = [3,1,2]

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        a,b = line.split(" ")
        b = b.strip()
        if b == "X":
            score += to_lose[values[a] -1]
        elif b == "Y":
            score += 3 + values[a]
        else:
            score += 6 + to_win[values[a] -1]
        line = file.readline()
print(score)