#Given a list of numbers, find the sum and average.

def sum(nums):
    sum = 0
    for index in range(len(nums)):
        sum += nums[index]
    return sum

def average(nums):
    sum = 0
    for index in range(len(nums)):
        sum += nums[index]
    return sum / len(nums)

def main():
    nums = [10, 20, 20, 10]
    a = average(nums)
    s = sum(nums)
    print("The average is ", a, ". The sum is ", s, " .")

if __name__ == "__main__":
    main()