""" app/calculator """

import sys
from ..operations.operations import Operations

class Calculator():
    """
    Central Interface Object for the Calculator program. Configures and maintains the REPL

    Attributes
    ----------

    op_dict : dict[str, Callable[str, float, float]]:
        A mapping of command strings to callable Operations functions

    Methods
    -------

    run() :
        Initiates the Calculator REPL
    """

    def __init__(self) -> None:
        """Instantiates the Calculator Object and prints introductory instructions"""
        self.op_dict: dict[str, Callable[str, float, float]] = {
                "add"       : Operations.add,
                "subtract"  : Operations.subtract,
                "multiply"  : Operations.multiply,
                "divide"    : Operations.divide
        }
        print("Welcome to Python REPL Calculator, v.1.3")
        print("Available Commands\
                \n\tadd <x> <y>\
                \n\tsubtract <x> <y>\
                \n\tmultiply <x> <y>\
                \n\tdivide <x> <y>\n")

    def run(self) -> None:
        """Launches the REPL"""
        while True:
            match input("$: ").lower().strip().split():
                case ["exit"]:
                    print("Thank you for using Python REPL Calculator. Exiting...")
                    break
                case [command, x, y]:
                    try:
                        operands = (float(x), float(y))
                    except ValueError:
                        print("Error: Operands <x>, <y> must be float-parsable.")
                        continue
                    if command in self.op_dict:
                        try:
                            result = self.op_dict[command](operands[0], operands[1])
                        except ZeroDivisionError:
                            print("Error: Cannot divide by zero.")
                            continue
                        if result.is_integer():
                            result = int(result)
                        print(f"Result: {result}")
                    else:
                        print(f"Error: No valid command <{command}>.") 
                case _:
                    print("Error: Invalid Command Syntax. Expected <command> <x> <y>.")
