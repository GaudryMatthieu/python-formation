#Write a program that checks if a given list is sorted in ascending order.

def ascending_order(nums):
    for index in range(1, len(nums)):
        if nums[index - 1] > nums[index]:
            return False
    return True

def main():
    nums = [1, 2, 3, 4, 5, 2]
    print("Is the list sorted in ascending order?", ascending_order(nums))

if __name__ == "__main__":
    main()