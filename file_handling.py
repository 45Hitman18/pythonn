# open a file in write mode (creates the file if it doesn't exist)
with open('example.txt', 'w') as file:
    file.write("hello, world!\n")
    file.write("this is a simple file handling example.\n")

# open the file in read mode and print content
with open('example.txt', 'r') as file:
    content = file.read()
    print("file content after writing:")
    print(content)

# open the file in append mode and add new content
with open('example.txt', 'a') as file:
    file.write("appending some new content!\n")

# open the file again in read mode to show the updated content
with open('example.txt', 'r') as file:
    content = file.read()
    print("\nfile content after appending:")
    print(content)

# open the file in read mode and read lines one by one
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("\nreading lines from the file:")
    for line in lines:
        print(line.strip())  # strip() removes the newline character
