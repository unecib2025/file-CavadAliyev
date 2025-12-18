with open("full_log.txt", "w") as out:
    for name in ["log1.txt", "log2.txt"]:
        with open(name, "r") as f:
            out.write(f.read())