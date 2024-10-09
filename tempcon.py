temp = float(input("Enter the temperature: "))

# celsius to fahrenheit
cf = (temp * 9/5) + 32
# fahrenheit to celsius
fc = (temp - 32) * 5/9

print(f"{temp}°C is equal to {cf}°F")
print(f"{temp}°F is equal to {fc}°C")
