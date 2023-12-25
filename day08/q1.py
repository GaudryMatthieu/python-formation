#Write a Python program to copy the contents of one text file into another.

def copy_file_to_other_file(file):
    file2 = open("file2.txt", "w+")
    file.seek(0)
    content = file.read()
    file2.write(content)

def create_file():
    file = open("file.txt", "w+")
    file.write("Hello world !")
    return file

def main():
    file = create_file()
    copy_file_to_other_file(file)

if __name__ == "__main__":
    main()