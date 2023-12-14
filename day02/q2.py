#Create a program that takes a temperature in Celsius and converts it to Kelvin.

def CelsiusToKelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def main():
    celsius = float(input("Enter the temperature in Celsius: "))
    kevin = CelsiusToKelvin(celsius)
    print("%.2f Celsius is equal to %.2f Kelvin" % (celsius, kevin))

if __name__ == "__main__":
    main()