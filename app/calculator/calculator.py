import sys
from ..operations.operations import Operations

class Calculator():
    def __init__(self) -> None:
        print("Welcome to Python REPL Calculator, v.1.2")
    def run(self) -> None:
        while True:
            user_input = input("$: ").lower().strip()
            if user_input == "exit":
                print("Thank you for using Python REPL Calculator. Exiting...")
                break
            try:
                command, x, y = user_input.split()
            except ValueError:
                print("Input Error: Expected '<command> <x> <y>'")
                continue
            try:
                x = float(x)
                y = float(y)
            except ValueError:
                print("Input Error: One or more operands not parsable.")
                continue
            match command:
                case 'add':
                    output = Operations.add(x, y)
                case 'subtract':
                    output = Operations.subtract(x, y)
                case 'multiply':
                    output = Operations.multiply(x, y)
                case 'divide':
                    if y == 0:
                        print("Input Error: Cannot Divide by Zero")
                        continue
                    output = Operations.divide(x, y)
                case _:
                    print("Input Error: Invalid Command")
                    continue
            if output.is_integer():
                output = int(output)
            print(f"Result: {output}")
