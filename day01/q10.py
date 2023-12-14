#Implement a program that swaps the values of two variables.

def swap(v1 , v2):
    v1, v2 = v2, v1
    return v1, v2

def main():
    v1 = 4
    v2 = 8
    v1, v2 = swap(v1, v2)
    print("The value of variable v1 is : ", v1)
    print("The value of variable v2 is : ", v2)

if __name__ == "__main__":
    main()