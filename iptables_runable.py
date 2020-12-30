import os

input_file = open(r"output_list.txt", "r")

text=input_file.readlines()

for i in text:
    i.strip()
    os.system(i)

os.system("echo Done")
input_file.close()