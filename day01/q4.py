#Given a list of numbers, find the maximum and minimum values. 

def min(nums):
    min = nums[0]
    for index in nums:
        if index < min:
            min = index
    print("The value minimum of your list is ", min)

def max(nums):
    max= nums[0]
    for index in nums:
        if index > max:
            max = index
    print("The value maximum of your list is ", max)

def main():
    nums = [12,34,56,78,90, -8]
    min(nums)
    max(nums)

if __name__ == "__main__":
    main()