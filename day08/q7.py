#Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file.

def create_file():
    file = open("file.txt", "w+")
    file.write("2 3 4 5 b 1 9 8 7 6 10")
    file.seek(0) 
    return file

def count(file):
    list = ""
    for line in file:
        list = line.split()
    sum = 0
    nums = "0123456789"
    for index in list:
        check = 0
        for num in nums:
            for element in index:
                if element == num:
                    check += 1
        if check == len(index):
            sum += int(index)
    return sum

def main():
    file = create_file()
    sum = count(file)
    print("The sum is", sum)

if __name__ == "__main__":
    main()