#Given two lists of numbers, concatenate them into a single list.

def concatenate(list1, list2):
    new_list = list1 + list2
    return new_list

def main():
    nums1 = [5, 3, 9]
    nums2 = [7, 4, 6, 8]
    new_list = concatenate(nums1, nums2)
    print("The concatenated list is:", new_list)

if __name__ == "__main__":
    main()