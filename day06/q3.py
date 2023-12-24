#Implement a function that takes a list of numbers and returns a new list with the squared values.

def square_values(numbers):
    for index in range(len(numbers)):
        numbers[index] = numbers[index] ** 2
    return numbers

def main():
    nums = [1, 2, 3, 4, 5]
    print("Original List:", nums)
    result = square_values(nums)
    print("Squared Values:", result)

if __name__ == "__main__":
    main()