with open("auth.log", "r") as inp, open("failed.txt", "w") as out:
    for line in inp:
        if "fail" in line.lower():
            out.write(line)