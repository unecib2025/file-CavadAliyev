with open("passwords.txt", "r") as a:
    with open("weak.txt", "w") as b:
        for c in a:
            if len(c.strip()) < 8:
                b.write(c)