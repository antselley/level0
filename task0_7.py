def celcius_to_farenheit(input_celcius):
    return input_celcius * 1.8 + 32

def farenheit_to_celcius(input_farenheit):
    return (input_farenheit - 32) * (5/9)

print(celcius_to_farenheit(50))
print(farenheit_to_celcius(81))