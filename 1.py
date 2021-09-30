with open("text1.txt") as file:
    for line in file:
        line = line.lstrip()
        line = line.rstrip()
        print(line)
