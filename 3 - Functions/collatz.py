def collatz(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return int(n / 2)
    else:
        return n*3+1

while True:
    print("Give me a number to generate the Collatz sequence:")
    try: 
        num = int(input())
        break
    except: print("invalid input, please enter a number")

while True:
    num = collatz(num)
    print(num)
    if num == 1:
        break
