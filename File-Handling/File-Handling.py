my_file = open("example.txt", mode="w+")
print("What is the file name? ", my_file.name)
print("What is the mode of the file? ", my_file.mode)
print("What is the encoding format?", my_file.encoding)


text = ["Hello Python\n", "Good Morning\n", "Good Bye"]
my_file.writelines(text)

print("Size of the file is:", my_file.__sizeof__())
print("Cursor position is at byte:", my_file.tell())

my_file.seek(0)
print("Content of the file is:", my_file.read())
my_file.close()


file = open("example.txt", mode="r")
line_number = 3
current_line = 1
data = ""

for line in file:
    if current_line == line_number:
        data = line
        print("Data present at current line is:", data)
        break
    current_line += 1
file.close()


bin_file = open("bfile.bin", mode="wb+")
message_content = data.encode("utf-32")
bin_file.write(message_content)

bin_file.seek(0)
bdata = bin_file.read()
print("Binary Data is:", bdata)

ndata = bdata.decode("utf-32")
print("Normal Data is:", ndata)

bin_file.close()
