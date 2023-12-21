#Create a function to find the square of each element in a given list.

def square(nums):
    new_list = []
    for index in nums:
         new_list.append(index ** 2)
    return new_list

def main():
    nums = [2, 0, -5, 6, 9, 10]
    print("Original List:",nums)
    squared_list = square(nums)
    print("\nSquared List:",squared_list)

if __name__ == "__main__":
    main()