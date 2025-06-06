import time, sys

indent = 0
indent_increasing = True

try:
    while True:
        print(" " * indent, end = "")
        print("********")
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit("\nPrograma interrompido pelo usuário")
