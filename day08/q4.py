#Create a function that takes a list of sentences and writes them to a new text file, each on a new line.

def create_file(sentences):
    file = open("file.txt", "w+")
    for sentence in sentences:
        string = sentence + "\n"
        file.write(string)

def main():
    sentences = {
        "This is the first sentence.",
        "And this is another one.",
        "Yet another sentence comes here."
    }
    create_file(sentences)

if __name__ == "__main__":
    main()