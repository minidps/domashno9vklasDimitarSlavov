input_file = open("writtenfile.txt", "r")
output_file = open("output.txt", "w")
lines = input_file.readlines()
i = 0
while i < len(lines):
    if i % 2 == 0:
        output_file.write(lines[i])
    i += 1
input_file.close()
output_file.close()