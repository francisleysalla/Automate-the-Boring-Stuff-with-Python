# List comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers, end="\n\n")

# Set comprehension
odd_squares = {x**2 for x in range(10) if x % 2 == 1}
print(odd_squares, end="\n\n")

# Dictionary comprehension
gals = ["Alejandra", "Paulina", "Daniela"]
instruments = ["Bass", "Drums", "Guitar"]
the_warning = {gals: instruments for gals, instruments in zip(gals, instruments)}
print(the_warning, end="\n\n")

# Generator expression
squares = ((x+1)**2 for x in range(10))
print(squares)
print(tuple(squares))