count = 0

with open("input.txt","r") as file:
    line = file.readline().strip()
    while line:
        line2 = file.readline().strip()
        line3 = file.readline().strip()
        letters = {}
        both = []
        final = ""
        for i in line:
            if i not in letters:
                letters[i] = 1
        for y in line2:
            if y in letters and y not in both:
                both.append(y)
        for z in line3:
            if z in both:
                final = z

        for x in final:
            val = ord(x)
            if val > 90:
                val = val  -96
            else:
                val = val - 38
            count+=val
        line = file.readline().strip()
print(count)