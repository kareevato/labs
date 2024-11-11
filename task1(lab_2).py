import math
# Введення даних
a = 4
b = 7
h = 0.2

x = a
while x <= b:
    if x < 4.5:
        y = 1 / math.cos(x * math.cos(x))  # sec(x*cos(x))
    elif 4.5 <= x < 6:
        y = x**3 + 4
    else:
        y = math.log(math.exp(x))  # lg(e^x)
    
    print(f"x: {x}, y: {y:.4f}")
    x += h 
    x = round(x,2)
    print(x)