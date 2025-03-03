file = open("data.txt", "w", encoding="UTF-8")

for i in range(1 , 101):
    text = f"Line {i}\n"
    file.write(text)

file.close