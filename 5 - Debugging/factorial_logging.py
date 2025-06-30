import logging

# This config of logging writes the debug messages on the console
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s = %(message)s') 

# This line disables all logging messages.
# logging.disable(logging.CRITICAL)

# This config of logging writes the debug messages on another file
logging.basicConfig(filename='5 - Debugging/factorial_logging_debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s = %(message)s') 

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')' )
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug("i is " + str(i) + ", total is " + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug("End of program")
