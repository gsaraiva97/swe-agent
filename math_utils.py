def divide(a, b):
    return a / b

def average(numbers):
    return sum(numbers) / len(numbers)

# Uso errado: pode causar ZeroDivisionError
print("Média:", average([]))
