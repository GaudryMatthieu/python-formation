#Given a list of integers, find the sum of all positive numbers.

def sort(nums):
    sum = 0
    for index in range(len(nums) - 1):
        if nums[index] > 0:
            sum += nums[index]
    return sum

def main():
    nums = [1, -2, 1, 1, -5, 1, -8, 0]
    sum = sort(nums)
    print("The sum of all the positive numbers of the list is ", sum)

if __name__ == "__main__":
    main()