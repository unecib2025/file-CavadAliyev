with open("traffic.txt", "r") as inp, open("alert.txt", "w") as out:
    for t in inp:
        if int(t.strip()) > 1000:
            out.write(t)