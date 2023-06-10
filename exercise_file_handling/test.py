import os
symbols = ["-", ",", ".", "!", "?"]

root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "1_text.txt"
text_file_path = os.path.join(root_dir, file_name)

with open(text_file_path, "r") as file:
    text = file.readlines()

for i in range(0, len(text), 2):

    for symbol in symbols:
        text[i] = text[i].replace(symbol, "@")

    print(*text[i].split()[::-1], sep=" ")
