import random

w = 0
l = 0
t = 0


def get_c_option():
    c = random.choice(['r','p','s'])
    if c == 'r':
        print("ROCK")
    elif c == 'p':
        print("PAPER")
    elif c == 's':
        print("SCISSORS")
    return c


print("ROCK, PAPER, SCISSORS")
while True:
    print(f"{w} wins, {l} losses, {t} ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    option = input()
    if option == 'q':
        break
    
    if option == 'p':
        print("PAPER versus...")
    elif option == 'r':
        print("ROCK versus...")
    elif option == 's':
        print("SCISSORS versus...")    

    c_option = get_c_option()

    if option == c_option:
        print("It's a tie!")
        t += 1
    elif (option == 'p' and c_option == 'r') or \
          (option == 's' and c_option == 'p') or \
          (option == 'r' and c_option == 's'):
        print("You win!")
        w += 1
    elif (option == 'r' and c_option == 'p') or \
         (option == 'p' and c_option == 's') or \
         (option == 's' and c_option == 'r'):
        print("You lose!")
        l += 1