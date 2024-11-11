import math

# Введення параметрів
a = -1
b = 1
h = 0.1
d = 0.001

# Табулювання функції
x = a
print(f"{'x':^10} {'term':^15} {'total':^15}")

while x <= b:
    total = 0.0
    k = 0
    

    while True:
        term = (x / (2 * k + 1) ** 3) * math.sin(2 * k + 1)
        if abs(term) < d:
            break
        total += term
        k += 1

    print(f"{x} {total}")
    x += h
    x= round (x,3)
    print(x)

for i in range(5):
    print(i)

print(f"\nФінальна сума: {total:.5f}")