def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    unit = input("Convert from Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")
    elif unit == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter C or F.")


if __name__ == "__main__":
    main()
