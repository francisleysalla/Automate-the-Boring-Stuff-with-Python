# This function show that immutable objects like integers cannot be modified by a function
def comer():
    comida = "Pizza"
    print(comida)

comida = "macarrão"
comer()
print(f"\nEstou comendo {comida}")

# This function modifies the global list 'bebida'
def beber_global():
    bebida.append("Chimarrão")

# This function prints the local list 'bebida'
def beber_local():
    bebida = ["Martini", "Vinho", "Pepsi", "Aguardente"] # Making a new attribution creates a local variable
    print("\nBebidas locais:")
    for b in bebida:
        print(b)

bebida = ["Cerveja", "whisky", "Coca-Cola", "Água"]

beber_global()
print("\nAs bebidas são:")
for b in bebida:
    print(b)

beber_local()