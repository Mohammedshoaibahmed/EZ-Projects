class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


if __name__ == "__main__":

    celsius_temperature = 25
    fahrenheit_temperature = TemperatureConverter.celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")

    # Convert Fahrenheit to Celsius
    fahrenheit_temperature = 77
    celsius_temperature = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")
