import sys

while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == 'exit':
        print("Exiting the program")
        sys.exit()
    print(f"You typed: {user_input}")