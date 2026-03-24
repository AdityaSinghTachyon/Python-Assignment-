from temperature import celsius_to_kelvin_coverter
from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
def main():
    while True:
        print("₹1. Celcius to Kelvin")
        print("2. Celcius to Fahrenheit")
        print("3. Fahrenheit to Celcius")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            celcius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Kelvin: ", celsius_to_kelvin_coverter.convert(celcius))
        elif choice == 2:
            celcius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Fahrenheit: ", celsius_to_fahrenheit.convert(celcius))
        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celcius: ",fahrenheit_to_celsius.convert(fahrenheit))
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
