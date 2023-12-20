#Given a list of numbers, create a function to find the sum of all positive numbers.

def sort(nums):
    sum = 0
    for index in range(len(nums)):
        if nums[index] > 0:
            sum += nums[index]
    return sum

def valid_number(string):
    try:
        number = int(input(string))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        return valid_number(string)

def nums_list():
    nums = []
    string = ["What is the lenght of your list : ", "Give me a number : "]
    lenght = valid_number(string[0])
    for i in range(lenght):
        nums.append(valid_number(string[1]))
    return nums

def main():
    nums = nums_list()
    sum = sort(nums)
    print("The sum of all the positive numbers of the list is ", sum)

if __name__ == "__main__":
    main()