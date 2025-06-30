def print_box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("The symbol should be a single character.")
    if width <= 2:
        raise Exception("The width should be greater than 2.")
    if height <= 2:
        raise Exception("The height should be greater than 2.")
    
    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    print_box('*', 5, 3)
    print_box('#', 10, 5)
    print_box('##', 10, 5) # Raises the first exception
    print_box('*', 1, 5) # Raises the second exception
    print_box('*', 5, 1) # Raises the third exception
except Exception as err:
    print("An Excetion occurred:", err)