#Create a program that takes a temperature in Celsius and converts it to Kelvin.

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def main():
    celsius = float(input("Enter the temperature in Celsius: "))
    kevin = celsius_to_kelvin(celsius)
    print("%.2f Celsius is equal to %.2f Kelvin" % (celsius, kevin))

if __name__ == "__main__":
    main()