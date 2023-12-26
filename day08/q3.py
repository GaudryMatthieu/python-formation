#Implement a program that reads a text file and counts the number of words and lines in it.

def count(sentence):
    words = sentence.split()#split the sentence into and insert the works into a list(understand the ' 's)
    return len(words)

def count_lines_and_words(file):
    lines = 0
    words = 0
    for line in file:
        lines += 1
        words += count(line)
    return lines, words

def create_file():
    file = open("file.txt", "w+")
    file.write("Hello world ! \n Voici une 2é ligne \n et encore une !!")
    file.seek(0)  # Move the cursor back to the beginning of the file for reading
    return file

def main():
    file = create_file()
    lines, words = count_lines_and_words(file)
    print("Lines:", lines, "\nWords:", words)

if __name__ == "__main__":
    main()