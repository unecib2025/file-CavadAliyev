with open("ips.txt", "r") as a:
    unique_ips = set(a.readlines())
with open("unique_ips.txt", "w") as b:
    b.writelines(unique_ips)