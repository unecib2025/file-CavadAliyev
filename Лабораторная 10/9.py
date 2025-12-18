with open("users.txt", "r") as f:
    count = len(f.readlines())
with open("report.txt", "w") as out:
    out.write(f"Всего пользователей: {count}")