#Write a program that converts a given number of days into years, weeks, and days.

def years(num):
    y = round(num / 365)
    print(y)
    r = num % 365
    print(r)
    return r, y

def weeks(r):
    w = round((r) / 7)
    r = (r) % 7
    return r, w

def main():
    num_days = int(input("Enter the number of days: ")) #I was lazy to do a verification again on the input
    r, y = years(num_days)
    d, w = weeks(r)
    print(num_days, " is equal to ", y, " years, ", w, " weeks and ", d, " days")

if __name__ == "__main__":
    main()