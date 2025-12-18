with open("ports.txt", "r") as inp, open("blocked_ports.txt", "w") as out:
    for port in inp:
        if int(port.strip()) < 1024:
            out.write(port)
