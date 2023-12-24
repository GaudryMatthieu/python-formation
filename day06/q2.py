#Write a program that finds the largest and smallest elements in a list.

def largest_element(list):
    max = list[0]
    for element in list:
        if element > max:
            max = element
    return max

def main():
    numbers = [5, 10, -3, 7, 2]
    result = largest_element(numbers)
    print("The largest number is", result)

if __name__ == "__main__":
    main()