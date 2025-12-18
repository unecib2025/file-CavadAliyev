with open("commands.txt", "r") as inp, open("safe.txt", "w") as out:
    for cmd in inp:
        if "rm" not in cmd:
            out.write(cmd)